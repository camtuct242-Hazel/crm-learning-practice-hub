// CRM Bilingual Learning & Practice Hub - Core Application Logic
(function () {
  'use strict';

  // --- STATE INITIALIZATION ---
  const STORAGE_KEY_LANG = 'crm_lang';
  const STORAGE_KEY_PROGRESS = 'crm_user_progress';

  const defaultProgress = {
    completedChapters: [],
    flashcardRatings: {}, // { [cardId]: 'again' | 'hard' | 'good' | 'easy' }
    examAttempts: {},     // { [examId]: { score: 18, total: 20, answers: {}, date: '...' } }
    caseNotes: {},        // { [caseId]: 'notes text' }
    caseWorkspaces: {}    // { [caseId]: { problemDefinition, ..., lastSaved } }
  };

  let savedProgress = JSON.parse(JSON.stringify(defaultProgress));
  try {
    const raw = localStorage.getItem(STORAGE_KEY_PROGRESS);
    if (raw) {
      const parsed = JSON.parse(raw);
      if (parsed && typeof parsed === 'object') {
        savedProgress = Object.assign({}, defaultProgress, parsed);
        if (!Array.isArray(savedProgress.completedChapters)) savedProgress.completedChapters = [];
        if (!savedProgress.flashcardRatings || typeof savedProgress.flashcardRatings !== 'object') savedProgress.flashcardRatings = {};
        if (!savedProgress.examAttempts || typeof savedProgress.examAttempts !== 'object') savedProgress.examAttempts = {};
        if (!savedProgress.caseNotes || typeof savedProgress.caseNotes !== 'object') savedProgress.caseNotes = {};
        if (!savedProgress.caseWorkspaces || typeof savedProgress.caseWorkspaces !== 'object') savedProgress.caseWorkspaces = {};
        // Backward-compat: migrate legacy caseNotes into caseWorkspaces
        Object.keys(savedProgress.caseNotes).forEach(cid => {
          if (!savedProgress.caseWorkspaces[cid]) {
            savedProgress.caseWorkspaces[cid] = { overallNotes: savedProgress.caseNotes[cid] };
          }
        });
      }
    }
  } catch (e) {
    console.warn('Could not load progress from localStorage, resetting to default', e);
    savedProgress = JSON.parse(JSON.stringify(defaultProgress));
  }

  const state = {
    currentLang: localStorage.getItem(STORAGE_KEY_LANG) || 'vi',
    activeTab: 'dashboard',
    activeChapterId: null,
    activeExamId: null,
    examAnswers: {}, // { [qId]: 'A' | 'B' | 'C' | 'D' }
    examSubmitted: false,
    practiceQuestions: [],
    practiceAnswers: {},
    practiceSubmitted: false,
    practiceFeedbackMode: 'instant',
    activeCaseId: null,
    caseReadingMode: 'original',
    caseModelAnswerRevealed: {},
    caseAiFeedback: {},
    caseAutoSaveTimer: null,
    flashcardIndex: 0,
    flashcardFlipped: false,
    flashcardFilterTopic: 'all',
    glossarySearchQuery: '',
    progress: savedProgress
  };

  // Helper to get bilingual text
  function t(path) {
    const keys = path.split('.');
    let curr = window.CRM_DATA?.translations;
    for (const k of keys) {
      if (!curr) return path;
      curr = curr[k];
    }
    if (curr && typeof curr === 'object') {
      return curr[state.currentLang] || curr.vi || curr.en || path;
    }
    return curr || path;
  }

  function getText(obj) {
    if (!obj) return '';
    if (typeof obj === 'string') return obj;
    return obj[state.currentLang] || obj.vi || obj.en || '';
  }

  // --- SAFE MARKDOWN RENDERER ---
  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function parseInline(text) {
    if (!text) return '';
    let s = escapeHtml(text);
    // Linkify URLs: https?://...
    s = s.replace(/(https?:\/\/[^\s<"')]+)/g, '<a href="$1" target="_blank" rel="noopener noreferrer" style="color: var(--accent-dark); text-decoration: underline; word-break: break-all;">$1</a>');
    // Inline code: `code`
    s = s.replace(/`([^`]+)`/g, '<code class="study-code">$1</code>');
    // Bold: **text**
    s = s.replace(/\*\*([^*]+)\*\*/g, '<strong class="study-strong">$1</strong>');
    // Italic: *text* (avoiding double asterisks)
    s = s.replace(/(?<!\*)\*([^*]+)\*(?!\*)/g, '<em class="study-em">$1</em>');
    return s;
  }

  function renderMarkdown(mdText) {
    if (!mdText) return '';

    // Split into subtopics by ### headings
    const rawSections = mdText.split(/^###\s+/m);
    const outHtml = [];

    for (let sIdx = 0; sIdx < rawSections.length; sIdx++) {
      const sec = rawSections[sIdx].trim();
      if (!sec) continue;

      const lines = sec.split('\n');
      let titleHtml = '';
      let bodyLines = [];

      if (sIdx === 0 && !mdText.trim().startsWith('###')) {
        bodyLines = lines;
      } else {
        const titleLine = lines[0].trim();
        bodyLines = lines.slice(1);
        titleHtml = `
          <div class="study-subtopic-header">
            <span class="subtopic-badge">📌</span>
            <h4 class="study-subtopic-title">${parseInline(titleLine)}</h4>
          </div>
        `;
      }

      const blocksHtml = [];
      let i = 0;
      while (i < bodyLines.length) {
        const line = bodyLines[i].trim();
        if (!line) {
          i++;
          continue;
        }

        // Unordered list: - or *
        if (/^[-*]\s+/.test(line)) {
          const listItems = [];
          while (i < bodyLines.length && /^[-*]\s+/.test(bodyLines[i].trim())) {
            const itemText = bodyLines[i].trim().replace(/^[-*]\s+/, '');
            listItems.push(`
              <li class="study-li">
                <span class="bullet-icon">✦</span>
                <div class="li-text">${parseInline(itemText)}</div>
              </li>
            `);
            i++;
          }
          blocksHtml.push(`<ul class="study-ul">${listItems.join('')}</ul>`);
          continue;
        }

        // Ordered list: 1. or 2.
        if (/^\d+\.\s+/.test(line)) {
          const listItems = [];
          while (i < bodyLines.length && /^\d+\.\s+/.test(bodyLines[i].trim())) {
            const m = bodyLines[i].trim().match(/^(\d+)\.\s+(.*)$/);
            const num = m ? m[1] : '';
            const itemText = m ? m[2] : bodyLines[i].trim();
            listItems.push(`
              <li class="study-li-ordered">
                <span class="num-badge">${num}</span>
                <div class="li-text">${parseInline(itemText)}</div>
              </li>
            `);
            i++;
          }
          blocksHtml.push(`<ol class="study-ol">${listItems.join('')}</ol>`);
          continue;
        }

        // Blockquote: >
        if (/^>\s+/.test(line)) {
          const quoteLines = [];
          while (i < bodyLines.length && /^>\s+/.test(bodyLines[i].trim())) {
            quoteLines.push(bodyLines[i].trim().replace(/^>\s+/, ''));
            i++;
          }
          blocksHtml.push(`
            <blockquote class="study-blockquote">
              <span class="quote-icon">💡</span>
              <div class="quote-text">${parseInline(quoteLines.join(' '))}</div>
            </blockquote>
          `);
          continue;
        }

        // Table row: | ... |
        if (/^\|.*\|$/.test(line)) {
          const tableRows = [];
          while (i < bodyLines.length && /^\|.*\|$/.test(bodyLines[i].trim())) {
            const rowLine = bodyLines[i].trim();
            if (!/^[|\s:-]+$/.test(rowLine)) {
              const cells = rowLine.split('|').slice(1, -1).map(c => c.trim());
              tableRows.push(cells);
            }
            i++;
          }
          if (tableRows.length > 0) {
            const headerRow = tableRows[0];
            const dataRows = tableRows.slice(1);
            const thead = `<tr>${headerRow.map(c => `<th>${parseInline(c)}</th>`).join('')}</tr>`;
            const tbody = dataRows.map(r => `<tr>${r.map(c => `<td>${parseInline(c)}</td>`).join('')}</tr>`).join('');
            blocksHtml.push(`
              <div class="study-table-wrap">
                <table class="study-table">
                  <thead>${thead}</thead>
                  <tbody>${tbody}</tbody>
                </table>
              </div>
            `);
          }
          continue;
        }

        // Regular paragraph: collect consecutive non-empty lines
        const pLines = [];
        while (
          i < bodyLines.length &&
          bodyLines[i].trim() &&
          !/^[-*]\s+/.test(bodyLines[i].trim()) &&
          !/^\d+\.\s+/.test(bodyLines[i].trim()) &&
          !/^>\s+/.test(bodyLines[i].trim()) &&
          !/^\|.*\|$/.test(bodyLines[i].trim())
        ) {
          pLines.push(bodyLines[i].trim());
          i++;
        }
        blocksHtml.push(`<p class="study-p">${parseInline(pLines.join(' '))}</p>`);
      }

      outHtml.push(`
        <article class="study-subtopic-card">
          ${titleHtml}
          <div class="study-subtopic-body">
            ${blocksHtml.join('')}
          </div>
        </article>
      `);
    }

    return outHtml.join('');
  }

  function saveProgress() {
    try {
      localStorage.setItem(STORAGE_KEY_PROGRESS, JSON.stringify(state.progress));
    } catch (e) {
      console.warn('Could not save progress', e);
    }
  }

  // Language Switcher - Never reloads page, preserves all in-progress forms/quizzes
  function setLanguage(lang) {
    if (lang !== 'vi' && lang !== 'en') return;
    state.currentLang = lang;
    try {
      localStorage.setItem(STORAGE_KEY_LANG, lang);
    } catch (e) {}

    // Update active state in toggle buttons
    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.lang === lang);
    });

    render();
  }

  // Tab Navigation
  function navigate(tab, detailId = null) {
    state.activeTab = tab;
    if (tab === 'library' && detailId) {
      state.activeChapterId = detailId;
    } else if (tab === 'exams' && detailId) {
      state.activeExamId = detailId;
      state.examAnswers = state.progress.examAttempts[detailId]?.answers || {};
      state.examSubmitted = !!state.progress.examAttempts[detailId];
    } else if (tab === 'cases' && detailId) {
      state.activeCaseId = detailId;
    }

    document.querySelectorAll('.nav-item').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.tab === tab);
    });

    render();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // --- VIEW RENDERERS ---

  function renderDashboard() {
    const data = window.CRM_DATA || {};
    const chaptersCount = data.curriculum?.length || 0;
    const termsCount = data.glossary?.length || 0;
    const cardsCount = data.flashcards?.length || 0;
    const questionsCount = (data.exams?.length || 10) * 20; // 200 questions target
    const examsCount = data.exams?.length || 10;
    const casesCount = data.cases?.length || 10;

    const completedChaps = state.progress.completedChapters.length;
    const completedExams = Object.keys(state.progress.examAttempts).length;
    const masteredCards = Object.values(state.progress.flashcardRatings).filter(r => r === 'easy' || r === 'good').length;

    return `
      <div class="view-card">
        <div class="view-header">
          <h1 class="view-title">${t('dashboard.welcomeTitle')}</h1>
          <p class="view-subtitle">${t('dashboard.welcomeDesc')}</p>
        </div>

        <div class="stats-grid">
          <div class="stat-box">
            <div class="stat-icon">📚</div>
            <div>
              <div class="stat-number">${chaptersCount}</div>
              <div class="stat-label">${t('dashboard.statChapters')}</div>
            </div>
          </div>
          <div class="stat-box">
            <div class="stat-icon">📖</div>
            <div>
              <div class="stat-number">${termsCount}</div>
              <div class="stat-label">${t('dashboard.statGlossary')}</div>
            </div>
          </div>
          <div class="stat-box">
            <div class="stat-icon">🎴</div>
            <div>
              <div class="stat-number">${cardsCount}</div>
              <div class="stat-label">${t('dashboard.statFlashcards')}</div>
            </div>
          </div>
          <div class="stat-box">
            <div class="stat-icon">🎯</div>
            <div>
              <div class="stat-number">${questionsCount}</div>
              <div class="stat-label">${t('dashboard.statQuestions')}</div>
            </div>
          </div>
          <div class="stat-box">
            <div class="stat-icon">📝</div>
            <div>
              <div class="stat-number">${examsCount}</div>
              <div class="stat-label">${t('dashboard.statExams')}</div>
            </div>
          </div>
          <div class="stat-box">
            <div class="stat-icon">🏢</div>
            <div>
              <div class="stat-number">${casesCount}</div>
              <div class="stat-label">${t('dashboard.statCases')}</div>
            </div>
          </div>
        </div>

        <div style="margin-top: 2rem;">
          <h3 style="margin-bottom: 1rem; color: var(--text-main); font-weight: 800;">${t('dashboard.quickActions')}</h3>
          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
            <button class="btn btn-primary" onclick="window.CRM_APP.navigate('library')">📚 ${t('nav.library')}</button>
            <button class="btn btn-primary" onclick="window.CRM_APP.navigate('flashcards')">🎴 ${t('dashboard.startFlashcards')}</button>
            <button class="btn btn-primary" onclick="window.CRM_APP.navigate('exams')">📝 ${t('dashboard.takeCuratedExam')}</button>
            <button class="btn btn-secondary" onclick="window.CRM_APP.navigate('practice')">🎲 ${t('dashboard.startRandomTest')}</button>
            <button class="btn btn-secondary" onclick="window.CRM_APP.navigate('cases')">🏢 ${t('dashboard.studyCase')}</button>
          </div>
        </div>

        <div style="margin-top: 2.5rem; background: var(--pastel-yellow-light); border: 1.5px solid var(--pastel-yellow); border-radius: var(--radius-lg); padding: 1.5rem; box-shadow: var(--shadow-xs);">
          <h3 style="margin-bottom: 0.85rem; color: var(--accent-dark); font-weight: 800;">⭐ ${t('dashboard.progressTitle')}</h3>
          <div style="display: flex; gap: 2.5rem; flex-wrap: wrap;">
            <div>
              <span style="font-weight: 700; color: var(--text-main);">${t('progress.chaptersStudied')}:</span> <strong style="color: var(--accent-dark);">${completedChaps} / ${chaptersCount}</strong>
            </div>
            <div>
              <span style="font-weight: 700; color: var(--text-main);">${t('progress.flashcardsMastered')}:</span> <strong style="color: var(--accent-dark);">${masteredCards} / ${cardsCount}</strong>
            </div>
            <div>
              <span style="font-weight: 700; color: var(--text-main);">${t('progress.examsCompleted')}:</span> <strong style="color: var(--accent-dark);">${completedExams} / ${examsCount}</strong>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  function renderLibrary() {
    const data = window.CRM_DATA || {};
    const modules = data.curriculum || [];

    if (state.activeChapterId) {
      const mod = modules.find(m => m.id === state.activeChapterId);
      if (mod) return renderChapterDetail(mod);
    }

    return `
      <div class="view-card">
        <div class="view-header">
          <h1 class="view-title">${t('library.title')}</h1>
          <p class="view-subtitle">${t('library.subtitle')}</p>
        </div>

        <div style="display: flex; flex-direction: column; gap: 1rem;">
          ${modules.map(mod => {
            const isCompleted = state.progress.completedChapters.includes(mod.id);
            return `
              <div style="border: 1.5px solid var(--border-color); border-radius: var(--radius-md); padding: 1.35rem; display: flex; justify-content: space-between; align-items: center; background: #FFFFFF; transition: all var(--transition-fast); box-shadow: var(--shadow-xs);" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.transform='translateY(-2px)';" onmouseout="this.style.borderColor='var(--border-color)'; this.style.transform='none';">
                <div style="padding-right: 1rem;">
                  <div class="stationery-tag" style="font-size: 0.72rem; margin-bottom: 0.35rem;">
                    ${getText(mod.part_title) || mod.book_title}
                  </div>
                  <h3 style="font-size: 1.15rem; color: var(--text-main); font-weight: 800; margin: 0.3rem 0;">
                    ${getText(mod.title)}
                  </h3>
                  <div style="font-size: 0.85rem; color: var(--text-muted);">
                    📖 ${mod.source?.document} — ${mod.source?.pages}
                  </div>
                </div>
                <div style="display: flex; align-items: center; gap: 0.85rem; flex-shrink: 0;">
                  ${isCompleted ? `<span class="chapter-status-pill status-completed">✓ ${t('library.completed')}</span>` : ''}
                  <button class="btn btn-secondary" onclick="window.CRM_APP.navigate('library', '${mod.id}')">
                    ${t('library.viewNotes')} →
                  </button>
                </div>
              </div>
            `;
          }).join('')}
        </div>
      </div>
    `;
  }

  function renderChapterDetail(mod) {
    const data = window.CRM_DATA || {};
    const modules = data.curriculum || [];
    const currentIndex = modules.findIndex(m => m.id === mod.id);
    const prevMod = currentIndex > 0 ? modules[currentIndex - 1] : null;
    const nextMod = currentIndex >= 0 && currentIndex < modules.length - 1 ? modules[currentIndex + 1] : null;

    const isCompleted = state.progress.completedChapters.includes(mod.id);
    const readingTimeMinutes = Math.max(5, Math.round((getText(mod.detailed_notes).length || 500) / 450));

    return `
      <div class="chapter-container">
        <!-- Top Navigation & Breadcrumbs Bar -->
        <div class="chapter-nav-bar">
          <button class="btn btn-secondary" onclick="window.CRM_APP.clearChapterDetail()">
            ← ${t('library.backToLibrary')}
          </button>
          <div style="display: flex; gap: 0.5rem; align-items: center;">
            ${prevMod ? `
              <button class="btn btn-secondary" style="padding: 0.45rem 0.9rem; font-size: 0.85rem;" onclick="window.CRM_APP.navigate('library', '${prevMod.id}')" title="${getText(prevMod.title)}">
                ← ${t('library.prevChapter')}
              </button>
            ` : ''}
            ${nextMod ? `
              <button class="btn btn-secondary" style="padding: 0.45rem 0.9rem; font-size: 0.85rem;" onclick="window.CRM_APP.navigate('library', '${nextMod.id}')" title="${getText(nextMod.title)}">
                ${t('library.nextChapter')} →
              </button>
            ` : ''}
          </div>
        </div>

        <!-- Chapter Hero Banner -->
        <header class="chapter-hero-card">
          <div class="chapter-part-label">
            📖 ${getText(mod.part_title) || mod.book_title}
          </div>
          <h1 class="chapter-main-title view-title">${getText(mod.title)}</h1>
          <div class="chapter-meta-pills">
            <span class="source-pill">
              📚 ${mod.source?.document} — ${mod.source?.pages}
            </span>
            <span class="source-pill">
              ⏱️ ~${readingTimeMinutes} ${t('library.readingTime')}
            </span>
            <span class="chapter-status-pill ${isCompleted ? 'status-completed' : 'status-in-progress'}">
              ${isCompleted ? `✓ ${t('library.completed')}` : `○ ${t('library.inProgress')}`}
            </span>
          </div>
        </header>

        <!-- Section 1: Learning Objectives -->
        ${(mod.learning_objectives?.[state.currentLang] || mod.learning_objectives?.vi || []).length > 0 ? `
          <section class="study-objectives-box">
            <h3 class="study-objectives-title">🎯 ${t('library.learningObjectives')}</h3>
            <ul class="study-objectives-list">
              ${(mod.learning_objectives?.[state.currentLang] || mod.learning_objectives?.vi || []).map(obj => `
                <li class="study-objective-item">
                  <span class="study-objective-check">✓</span>
                  <div>${escapeHtml(obj)}</div>
                </li>
              `).join('')}
            </ul>
          </section>
        ` : ''}

        <!-- Section 2: Core Concepts -->
        ${(mod.key_concepts || []).length > 0 ? `
          <section class="study-concepts-section">
            <h3 class="study-section-title">💡 ${t('library.keyConcepts')}</h3>
            <div class="concept-grid">
              ${(mod.key_concepts || []).map(kc => `
                <div class="concept-card">
                  <div>
                    <div class="concept-card-header">
                      <h4 class="concept-name">${getText(kc.name)}</h4>
                      ${kc.term ? `<span class="concept-term-tag">${escapeHtml(kc.term)}</span>` : ''}
                    </div>
                    <p class="concept-definition">${getText(kc.definition)}</p>
                  </div>
                </div>
              `).join('')}
            </div>
          </section>
        ` : ''}

        <!-- Section 3: Detailed Study Notes (Parsed Markdown Subtopics) -->
        <section class="study-notes-section">
          <h3 class="study-section-title">📝 ${t('library.studyNotes')}</h3>
          <div class="study-content-flow">
            ${renderMarkdown(getText(mod.detailed_notes))}
          </div>
        </section>

        <!-- Section 4: Key Takeaways -->
        ${(mod.key_takeaways?.[state.currentLang] || mod.key_takeaways?.vi || []).length > 0 ? `
          <section class="study-takeaways-box">
            <h3 class="study-takeaways-title">⭐ ${t('library.keyTakeaways')}</h3>
            <ul class="study-takeaways-list">
              ${(mod.key_takeaways?.[state.currentLang] || mod.key_takeaways?.vi || []).map(kt => `
                <li class="study-takeaway-item">
                  <span style="color: #EAB308; font-size: 1.1rem; flex-shrink: 0;">★</span>
                  <div>${escapeHtml(kt)}</div>
                </li>
              `).join('')}
            </ul>
          </section>
        ` : ''}

        <!-- Section 5: Review Questions -->
        ${(mod.review_questions || []).length > 0 ? `
          <section style="margin-bottom: 2.25rem;">
            <h3 class="study-section-title">❓ ${t('library.reviewQuestions')}</h3>
            <div style="display: flex; flex-direction: column; gap: 1rem;">
              ${(mod.review_questions || []).map((rq, idx) => `
                <div class="study-review-card">
                  <div style="font-size: 0.78rem; font-weight: 800; color: var(--accent-dark); text-transform: uppercase; margin-bottom: 0.35rem;">
                    ${state.currentLang === 'vi' ? `Câu hỏi Ôn tập #${idx + 1}` : `Review Question #${idx + 1}`}
                  </div>
                  <p class="study-review-q">${getText(rq.question)}</p>
                  <div class="study-review-answer">
                    <strong style="color: var(--accent-dark);">${t('library.modelAnswer')}:</strong> ${getText(rq.model_answer)}
                  </div>
                </div>
              `).join('')}
            </div>
          </section>
        ` : ''}

        <!-- Bottom Action Bar -->
        <div class="chapter-action-bar">
          <div>
            ${prevMod ? `
              <button class="btn btn-secondary" onclick="window.CRM_APP.navigate('library', '${prevMod.id}')">
                ← ${getText(prevMod.title)}
              </button>
            ` : '<div></div>'}
          </div>

          <button class="btn ${isCompleted ? 'btn-secondary' : 'btn-primary'}" onclick="window.CRM_APP.toggleChapterCompleted('${mod.id}')">
            ${isCompleted ? `✓ ${t('library.completed')}` : `✔ ${t('library.markCompleted')}`}
          </button>

          <div>
            ${nextMod ? `
              <button class="btn btn-primary" onclick="window.CRM_APP.navigate('library', '${nextMod.id}')">
                ${getText(nextMod.title)} →
              </button>
            ` : '<div></div>'}
          </div>
        </div>
      </div>
    `;
  }

  function renderGlossary() {
    const data = window.CRM_DATA || {};
    const terms = data.glossary || [];
    const q = (state.glossarySearchQuery || '').toLowerCase();

    const filtered = terms.filter(item => {
      const viTerm = (item.term?.vi || '').toLowerCase();
      const enTerm = (item.term?.en || '').toLowerCase();
      const acronym = (item.acronym || '').toLowerCase();
      return viTerm.includes(q) || enTerm.includes(q) || acronym.includes(q);
    });

    return `
      <div class="view-card">
        <div class="view-header">
          <h1 class="view-title">${t('glossary.title')}</h1>
          <p class="view-subtitle">${t('glossary.subtitle')}</p>
        </div>

        <div style="margin-bottom: 1.5rem;">
          <input
            type="text"
            class="input-search"
            style="width: 100%; max-width: 500px; padding: 0.65rem 1rem; border: 1px solid var(--border); border-radius: var(--radius-md); font-size: 0.95rem;"
            placeholder="${t('glossary.search')}"
            value="${state.glossarySearchQuery}"
            oninput="window.CRM_APP.setGlossarySearch(this.value)"
          />
        </div>

        <div style="display: flex; flex-direction: column; gap: 1rem;">
          ${filtered.length === 0 ? `<p style="color: var(--text-muted);">${t('common.noData')}</p>` : ''}
          ${filtered.map(item => `
            <div class="term-card" style="border: 1px solid var(--border); border-radius: var(--radius-md); padding: 1.25rem; background: #fff;">
              <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 0.35rem;">
                <h3 style="color: var(--primary); font-size: 1.15rem;">${getText(item.term)}</h3>
                ${item.acronym ? `<span style="background: #e0f2fe; color: var(--secondary); font-weight: 700; font-size: 0.8rem; padding: 0.2rem 0.5rem; border-radius: var(--radius-sm);">${item.acronym}</span>` : ''}
              </div>
              <p style="font-size: 0.95rem; margin-bottom: 0.5rem; color: var(--text-main);">
                <strong>${t('glossary.definition')}:</strong> ${getText(item.definition)}
              </p>
              <p style="font-size: 0.85rem; color: #475569; margin-bottom: 0.5rem;">
                <strong>${t('glossary.context')}:</strong> ${getText(item.context)}
              </p>
              <div style="font-size: 0.75rem; color: var(--text-muted);">
                📖 ${item.source?.document}
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }

  function renderFlashcards() {
    const data = window.CRM_DATA || {};
    const cards = data.flashcards || [];

    if (cards.length === 0) {
      return `
        <div class="view-card">
          <div class="view-header">
            <h1 class="view-title">${t('flashcards.title')}</h1>
          </div>
          <p>${t('common.noData')}</p>
        </div>
      `;
    }

    const currCard = cards[state.flashcardIndex] || cards[0];
    const isFlipped = state.flashcardFlipped;

    return `
      <div class="view-card">
        <div class="view-header">
          <h1 class="view-title">${t('flashcards.title')}</h1>
          <p class="view-subtitle">${t('flashcards.subtitle')}</p>
        </div>

        <div class="flashcard-container">
          <div style="display: flex; justify-content: space-between; width: 100%; align-items: center;">
            <span style="font-size: 0.9rem; font-weight: 600; color: var(--text-muted);">
              ${t('flashcards.cardCount')} ${state.flashcardIndex + 1} / ${cards.length}
            </span>
            <span style="font-size: 0.8rem; font-weight: 600; color: var(--secondary); background: #f0f9ff; padding: 0.2rem 0.5rem; border-radius: var(--radius-sm);">
              ${currCard.topic || 'General'}
            </span>
          </div>

          <div class="flashcard flashcard-card ${isFlipped ? 'flipped' : ''}" onclick="window.CRM_APP.flipFlashcard()">
            <div class="flashcard-inner">
              <div class="flashcard-front">
                <div class="flashcard-badge">${state.currentLang === 'vi' ? 'CÂU HỎI / KHÁI NIỆM' : 'QUESTION / CONCEPT'}</div>
                <div class="flashcard-text">${getText(currCard.front)}</div>
                <div class="flashcard-hint">${t('flashcards.flipHint')}</div>
              </div>
              <div class="flashcard-back">
                <div class="flashcard-badge" style="color: var(--success); background: #dcfce7;">
                  ${state.currentLang === 'vi' ? 'ĐÁP ÁN / GIẢI THÍCH' : 'ANSWER / EXPLANATION'}
                </div>
                <div class="flashcard-text">${getText(currCard.back)}</div>
                ${currCard.hint ? `<div class="flashcard-hint">💡 ${getText(currCard.hint)}</div>` : ''}
              </div>
            </div>
          </div>

          <div class="flashcard-actions">
            <button class="rating-btn rating-again" onclick="window.CRM_APP.rateFlashcard('again')">${t('flashcards.ratingAgain')}</button>
            <button class="rating-btn rating-hard" onclick="window.CRM_APP.rateFlashcard('hard')">${t('flashcards.ratingHard')}</button>
            <button class="rating-btn rating-good" onclick="window.CRM_APP.rateFlashcard('good')">${t('flashcards.ratingGood')}</button>
            <button class="rating-btn rating-easy" onclick="window.CRM_APP.rateFlashcard('easy')">${t('flashcards.ratingEasy')}</button>
          </div>

          <div style="display: flex; gap: 1rem; margin-top: 0.5rem;">
            <button class="btn btn-secondary" onclick="window.CRM_APP.prevFlashcard()">← ${t('flashcards.prevCard')}</button>
            <button class="btn btn-secondary" onclick="window.CRM_APP.nextFlashcard()">${t('flashcards.nextCard')} →</button>
          </div>
        </div>
      </div>
    `;
  }

  function renderExams() {
    const data = window.CRM_DATA || {};
    const examsList = data.exams || [];

    if (state.activeExamId) {
      const activeExam = examsList.find(e => e.id === state.activeExamId);
      if (activeExam) return renderExamRunner(activeExam);
    }

    return `
      <div class="view-card">
        <div class="view-header">
          <h1 class="view-title">${t('exams.title')}</h1>
          <p class="view-subtitle">${t('exams.subtitle')}</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.25rem;">
          ${examsList.map(exam => {
            const attempt = state.progress.examAttempts[exam.id];
            const hasScore = !!attempt;
            return `
              <div style="border: 1px solid var(--border); border-radius: var(--radius-md); padding: 1.25rem; background: #fff; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <div style="font-size: 0.8rem; font-weight: 700; color: var(--secondary); text-transform: uppercase; margin-bottom: 0.25rem;">
                    ${exam.target_domain}
                  </div>
                  <h3 style="color: var(--primary); font-size: 1.15rem; margin-bottom: 0.5rem;">
                    ${getText(exam.title)}
                  </h3>
                  <p style="font-size: 0.9rem; color: #475569; margin-bottom: 1rem;">
                    ${getText(exam.description)}
                  </p>
                </div>

                <div>
                  <div style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 0.75rem;">
                    ⏱️ ${exam.time_limit_minutes} ${state.currentLang === 'vi' ? 'phút' : 'mins'} | 🎯 20 ${state.currentLang === 'vi' ? 'câu hỏi' : 'questions'}
                  </div>

                  ${hasScore ? `
                    <div style="font-size: 0.85rem; font-weight: 600; color: var(--success); margin-bottom: 0.75rem;">
                      ${t('exams.highestScore')} ${attempt.score} / ${attempt.total} (${Math.round(attempt.score / attempt.total * 100)}%)
                    </div>
                  ` : ''}

                  <button class="btn btn-primary" style="width: 100%;" onclick="window.CRM_APP.navigate('exams', '${exam.id}')">
                    ${hasScore ? t('exams.retake') : t('exams.startExam')} →
                  </button>
                </div>
              </div>
            `;
          }).join('')}
        </div>
      </div>
    `;
  }

  function renderExamRunner(exam) {
    const data = window.CRM_DATA || {};
    const allQuestions = data.questionBank || [];
    // Filter questions mapped to this exam
    const examQuestions = allQuestions.filter(q => q.exam_id === exam.id || exam.question_ids?.includes(q.id));

    // Calculate current score if submitted
    let score = 0;
    if (state.examSubmitted) {
      examQuestions.forEach(q => {
        if (state.examAnswers[q.id] === q.correct_answer) score++;
      });
    }

    return `
      <div class="view-card">
        <div style="margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: center;">
          <button class="btn btn-secondary" onclick="window.CRM_APP.clearExamRunner()">← ${t('common.back')}</button>
          <div style="font-weight: 600; color: var(--secondary);">
            ${examQuestions.length} ${state.currentLang === 'vi' ? 'Câu hỏi' : 'Questions'}
          </div>
        </div>

        <div class="view-header">
          <h1 class="view-title">${getText(exam.title)}</h1>
          <p class="view-subtitle">${getText(exam.description)}</p>
        </div>

        ${state.examSubmitted ? `
          <div style="margin-bottom: 2rem; background: ${score >= examQuestions.length * 0.75 ? '#ecfdf5' : '#fef2f2'}; border: 1px solid ${score >= examQuestions.length * 0.75 ? '#6ee7b7' : '#fca5a5'}; border-radius: var(--radius-md); padding: 1.5rem; text-align: center;">
            <h2 style="font-size: 1.5rem; color: ${score >= examQuestions.length * 0.75 ? '#065f46' : '#991b1b'}; margin-bottom: 0.5rem;">
              ${score >= examQuestions.length * 0.75 ? t('exams.passed') : t('exams.failed')}
            </h2>
            <div style="font-size: 1.25rem; font-weight: 700;">
              ${t('exams.scoreLabel')} ${score} / ${examQuestions.length} (${Math.round((score / (examQuestions.length || 1)) * 100)}%)
            </div>
          </div>
        ` : ''}

        <div style="display: flex; flex-direction: column; gap: 1.5rem;">
          ${examQuestions.map((q, idx) => {
            const selectedOpt = state.examAnswers[q.id];
            const isSubmitted = state.examSubmitted;

            return `
              <div class="question-card" id="card-${q.id}">
                <div class="question-header">
                  <span class="question-topic">${q.topic || 'General'}</span>
                  <span style="font-size: 0.8rem; font-weight: 600; color: var(--text-muted);">${t('exams.questionNum')} ${idx + 1}</span>
                </div>
                <div class="question-text">${getText(q.question)}</div>

                <div class="options-list">
                  ${(q.options || []).map(opt => {
                    const isSelected = selectedOpt === opt.id;
                    let extraClass = '';
                    if (isSubmitted) {
                      if (opt.id === q.correct_answer) extraClass = 'correct';
                      else if (isSelected && opt.id !== q.correct_answer) extraClass = 'incorrect';
                    } else if (isSelected) {
                      extraClass = 'selected';
                    }

                    return `
                      <div class="option-item ${extraClass}" onclick="window.CRM_APP.selectExamOption('${q.id}', '${opt.id}')">
                        <div class="option-key">${opt.id}.</div>
                        <div class="option-text">${getText(opt.text)}</div>
                      </div>
                    `;
                  }).join('')}
                </div>

                ${isSubmitted ? `
                  <div class="explanation-box">
                    <strong style="color: var(--primary);">${t('exams.explanation')}</strong>
                    <div style="margin-top: 0.35rem; color: #334155;">${getText(q.explanation)}</div>
                    <div class="source-pill" style="margin-top: 0.5rem;">
                      📖 ${q.source?.document} — ${q.source?.chapter} (${q.source?.pages})
                    </div>
                  </div>
                ` : ''}
              </div>
            `;
          }).join('')}
        </div>

        <div style="margin-top: 2rem; display: flex; justify-content: flex-end; gap: 1rem; border-top: 1px solid var(--border); padding-top: 1.5rem;">
          ${!state.examSubmitted ? `
            <button class="btn btn-primary" style="padding: 0.75rem 2rem; font-size: 1rem;" onclick="window.CRM_APP.submitExam('${exam.id}', ${examQuestions.length})">
              ✓ ${t('exams.submitExam')}
            </button>
          ` : `
            <button class="btn btn-secondary" onclick="window.CRM_APP.retakeExam('${exam.id}')">
              🔄 ${t('exams.retake')}
            </button>
          `}
        </div>
      </div>
    `;
  }

  function renderPractice() {
    if (state.practiceQuestions && state.practiceQuestions.length > 0) {
      return renderPracticeRunner();
    }

    return `
      <div class="view-card">
        <div class="view-header">
          <h1 class="view-title">${t('practice.title')}</h1>
          <p class="view-subtitle">${t('practice.subtitle')}</p>
        </div>

        <div style="max-width: 600px; background: #fff; border: 1px solid var(--border); border-radius: var(--radius-md); padding: 1.5rem;">
          <h3 style="color: var(--primary); margin-bottom: 1.25rem;">${t('practice.configTitle')}</h3>

          <div style="margin-bottom: 1rem;">
            <label style="display: block; font-weight: 600; margin-bottom: 0.35rem;">${t('practice.numQuestions')}</label>
            <select id="practice-count" style="width: 100%; padding: 0.5rem; border: 1px solid var(--border); border-radius: var(--radius-sm);">
              <option value="10">10 ${state.currentLang === 'vi' ? 'Câu hỏi' : 'Questions'}</option>
              <option value="20" selected>20 ${state.currentLang === 'vi' ? 'Câu hỏi' : 'Questions'}</option>
              <option value="30">30 ${state.currentLang === 'vi' ? 'Câu hỏi' : 'Questions'}</option>
            </select>
          </div>

          <div style="margin-bottom: 1rem;">
            <label style="display: block; font-weight: 600; margin-bottom: 0.35rem;">${t('practice.difficulty')}</label>
            <select id="practice-diff" style="width: 100%; padding: 0.5rem; border: 1px solid var(--border); border-radius: var(--radius-sm);">
              <option value="all">${t('practice.diffAll')}</option>
              <option value="easy">${t('practice.diffEasy')}</option>
              <option value="medium">${t('practice.diffMedium')}</option>
              <option value="hard">${t('practice.diffHard')}</option>
            </select>
          </div>

          <div style="margin-bottom: 1.5rem;">
            <label style="display: block; font-weight: 600; margin-bottom: 0.35rem;">${t('practice.mode')}</label>
            <select id="practice-mode" style="width: 100%; padding: 0.5rem; border: 1px solid var(--border); border-radius: var(--radius-sm);">
              <option value="instant">${t('practice.modeInstant')}</option>
              <option value="exam">${t('practice.modeExam')}</option>
            </select>
          </div>

          <button class="btn btn-primary" style="width: 100%; font-size: 1rem; padding: 0.75rem;" onclick="window.CRM_APP.startRandomPractice()">
            🚀 ${t('practice.startPractice')}
          </button>
        </div>
      </div>
    `;
  }

  function renderPracticeRunner() {
    const questions = state.practiceQuestions || [];
    const isInstant = state.practiceFeedbackMode === 'instant';
    const isSubmitted = state.practiceSubmitted;

    let score = 0;
    let answeredCount = 0;
    questions.forEach(q => {
      if (state.practiceAnswers[q.id]) {
        answeredCount++;
        if (state.practiceAnswers[q.id] === q.correct_answer) score++;
      }
    });

    return `
      <div class="view-card">
        <div style="margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
          <button class="btn btn-secondary" onclick="window.CRM_APP.exitPractice()">← ${state.currentLang === 'vi' ? 'Thoát Luyện tập' : 'Exit Practice'}</button>
          <div style="font-weight: 600; color: var(--secondary); display: flex; gap: 1rem; align-items: center;">
            <span>${questions.length} ${state.currentLang === 'vi' ? 'câu hỏi' : 'questions'} (${state.practiceFeedbackMode.toUpperCase()})</span>
            ${isInstant ? `<span style="background: #f1f5f9; padding: 0.25rem 0.6rem; border-radius: var(--radius-sm); color: var(--primary);">🎯 ${state.currentLang === 'vi' ? 'Đúng' : 'Score'}: ${score} / ${answeredCount}</span>` : ''}
          </div>
        </div>

        <div class="view-header">
          <h1 class="view-title">${state.currentLang === 'vi' ? 'Đề Luyện Tập Ngẫu Nhiên' : 'Random Practice Session'}</h1>
          <p class="view-subtitle">${isInstant 
            ? (state.currentLang === 'vi' ? 'Chế độ phản hồi tức thì: Chọn đáp án để xem giải thích và nguồn trích dẫn ngay lập tức.' : 'Instant Feedback Mode: Select an option to reveal rationales and source citations immediately.')
            : (state.currentLang === 'vi' ? 'Chế độ thi thử: Hoàn thành toàn bộ câu hỏi và bấm Nộp bài để xem điểm.' : 'Exam Mode: Complete all questions and click Submit to reveal your final score.')
          }</p>
        </div>

        ${isSubmitted ? `
          <div style="margin-bottom: 2rem; background: ${score >= questions.length * 0.75 ? '#ecfdf5' : '#fef2f2'}; border: 1px solid ${score >= questions.length * 0.75 ? '#6ee7b7' : '#fca5a5'}; border-radius: var(--radius-md); padding: 1.5rem; text-align: center;">
            <h2 style="font-size: 1.5rem; color: ${score >= questions.length * 0.75 ? '#065f46' : '#991b1b'}; margin-bottom: 0.5rem;">
              ${score >= questions.length * 0.75 ? (state.currentLang === 'vi' ? 'Xuất Sắc! Bạn Đã Đạt Chuẩn' : 'Passed with Excellence!') : (state.currentLang === 'vi' ? 'Cần Tiếp Tục Ôn Luyện' : 'Needs Further Review')}
            </h2>
            <div style="font-size: 1.25rem; font-weight: 700;">
              ${state.currentLang === 'vi' ? 'Điểm số của bạn:' : 'Your Score:'} ${score} / ${questions.length} (${Math.round((score / (questions.length || 1)) * 100)}%)
            </div>
          </div>
        ` : ''}

        <div style="display: flex; flex-direction: column; gap: 1.5rem;">
          ${questions.map((q, idx) => {
            const selectedOpt = state.practiceAnswers[q.id];
            const showFeedback = isInstant ? !!selectedOpt : isSubmitted;

            return `
              <div class="question-card" id="practice-card-${q.id}">
                <div class="question-header">
                  <span class="question-topic">${q.topic || 'General'}</span>
                  <span style="font-size: 0.8rem; font-weight: 600; color: var(--text-muted);">${t('exams.questionNum')} ${idx + 1}</span>
                </div>
                <div class="question-text">${getText(q.question)}</div>

                <div class="options-list">
                  ${(q.options || []).map(opt => {
                    const isSelected = selectedOpt === opt.id;
                    let extraClass = '';
                    if (showFeedback) {
                      if (opt.id === q.correct_answer) extraClass = 'correct';
                      else if (isSelected && opt.id !== q.correct_answer) extraClass = 'incorrect';
                    } else if (isSelected) {
                      extraClass = 'selected';
                    }

                    return `
                      <div class="option-item ${extraClass}" onclick="window.CRM_APP.selectPracticeOption('${q.id}', '${opt.id}')">
                        <div class="option-key">${opt.id}.</div>
                        <div class="option-text">${getText(opt.text)}</div>
                      </div>
                    `;
                  }).join('')}
                </div>

                ${showFeedback ? `
                  <div class="explanation-box" style="margin-top: 1rem;">
                    <div style="font-weight: 700; color: ${selectedOpt === q.correct_answer ? '#065f46' : '#b91c1c'}; margin-bottom: 0.35rem;">
                      ${selectedOpt === q.correct_answer ? '✓ ' + (state.currentLang === 'vi' ? 'Chính xác!' : 'Correct!') : '✗ ' + (state.currentLang === 'vi' ? 'Chưa chính xác! Đáp án đúng là ' + q.correct_answer : 'Incorrect! Correct answer is ' + q.correct_answer)}
                    </div>
                    <div style="color: #334155; line-height: 1.6;">${getText(q.explanation)}</div>
                    <div class="source-pill" style="margin-top: 0.6rem;">
                      📖 ${q.source?.document} — ${q.source?.chapter} (${q.source?.pages})
                    </div>
                  </div>
                ` : ''}
              </div>
            `;
          }).join('')}
        </div>

        <div style="margin-top: 2rem; display: flex; justify-content: flex-end; gap: 1rem; border-top: 1px solid var(--border); padding-top: 1.5rem;">
          ${!isInstant && !isSubmitted ? `
            <button class="btn btn-primary" style="padding: 0.75rem 2rem; font-size: 1rem;" onclick="window.CRM_APP.submitPractice(${questions.length})">
              ✓ ${state.currentLang === 'vi' ? 'Nộp Bài Luyện Tập' : 'Submit Practice Test'}
            </button>
          ` : `
            <button class="btn btn-secondary" onclick="window.CRM_APP.exitPractice()">
              🔄 ${state.currentLang === 'vi' ? 'Luyện Đề Khác' : 'Start Another Session'}
            </button>
          `}
        </div>
      </div>
    `;
  }

  // --- CASE STUDY LAB: VERBATIM LOUNGE, 10-DIM WORKSPACE & SOCRATIC AI ---
  function renderCaseMarkdown(text) {
    if (!text) return '';
    const lines = text.split('\n');
    let html = '';
    let inList = false;
    let listType = 'ul';

    for (let i = 0; i < lines.length; i++) {
      let line = lines[i].trim();
      if (!line) {
        if (inList) {
          html += `</${listType}>\n`;
          inList = false;
        }
        continue;
      }

      // Horizontal Rule
      if (/^(\-{3,}|\*{3,}|_{3,})$/.test(line)) {
        if (inList) { html += `</${listType}>\n`; inList = false; }
        html += '<hr style="margin: 1.5rem 0; border: none; border-top: 1.5px solid var(--border-subtle, #e2e8f0);"/>\n';
        continue;
      }

      // Markdown Table
      if (/^\|.*\|$/.test(line)) {
        if (inList) { html += `</${listType}>\n`; inList = false; }
        const tableRows = [];
        while (i < lines.length && /^\|.*\|$/.test(lines[i].trim())) {
          const rowLine = lines[i].trim();
          if (!/^[|\s:-]+$/.test(rowLine)) {
            const cells = rowLine.split('|').slice(1, -1).map(c => c.trim());
            tableRows.push(cells);
          }
          i++;
        }
        i--; // Step back one because outer loop will increment
        if (tableRows.length > 0) {
          const headerRow = tableRows[0];
          const dataRows = tableRows.slice(1);
          const thead = `<tr>${headerRow.map(c => `<th style="padding: 0.6rem 0.85rem; border: 1px solid var(--border, #cbd5e1); font-weight: 700; text-align: left; background: var(--bg-warm, #fef9c3); color: var(--text-heading, #1e293b);">${parseInline(c)}</th>`).join('')}</tr>`;
          const tbody = dataRows.map(r => `<tr>${r.map(c => `<td style="padding: 0.55rem 0.85rem; border: 1px solid var(--border, #cbd5e1); color: var(--text-main, #334155);">${parseInline(c)}</td>`).join('')}</tr>`).join('');
          html += `
            <div class="study-table-wrap" style="overflow-x: auto; margin: 1.25rem 0; border-radius: var(--radius-sm, 6px); box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
              <table class="study-table" style="width: 100%; border-collapse: collapse; font-size: 0.88rem; background: #ffffff;">
                <thead>${thead}</thead>
                <tbody>${tbody}</tbody>
              </table>
            </div>\n`;
        }
        continue;
      }

      // Headings
      if (line.startsWith('#### ')) {
        if (inList) { html += `</${listType}>\n`; inList = false; }
        html += `<h4 style="margin: 1.2rem 0 0.5rem 0; font-size: 1.05rem; color: var(--accent-dark, #854d0e); font-weight: 700;">${parseInline(line.substring(5))}</h4>\n`;
      } else if (line.startsWith('### ')) {
        if (inList) { html += `</${listType}>\n`; inList = false; }
        html += `<h3 style="margin: 1.5rem 0 0.6rem 0; font-size: 1.2rem; color: var(--accent-dark, #854d0e); font-weight: 700; border-bottom: 1px solid var(--border-subtle, #f1f5f9); padding-bottom: 0.35rem;">${parseInline(line.substring(4))}</h3>\n`;
      } else if (line.startsWith('## ')) {
        if (inList) { html += `</${listType}>\n`; inList = false; }
        html += `<h2 style="margin: 1.8rem 0 0.8rem 0; font-size: 1.4rem; color: var(--text-heading, #1e293b); font-weight: 800;">${parseInline(line.substring(3))}</h2>\n`;
      } else if (line.startsWith('# ')) {
        if (inList) { html += `</${listType}>\n`; inList = false; }
        html += `<h1 style="margin: 2rem 0 1rem 0; font-size: 1.6rem; color: var(--text-heading, #1e293b); font-weight: 800;">${parseInline(line.substring(2))}</h1>\n`;
      } else if (/^>\s+/.test(line)) {
        if (inList) { html += `</${listType}>\n`; inList = false; }
        const quoteLines = [];
        while (i < lines.length && /^>\s+/.test(lines[i].trim())) {
          quoteLines.push(lines[i].trim().replace(/^>\s+/, ''));
          i++;
        }
        i--;
        html += `<blockquote style="margin: 1rem 0; padding: 0.75rem 1.2rem; border-left: 4px solid var(--accent-gold, #ca8a04); background: var(--bg-card-subtle, #fefce8); border-radius: 4px; font-style: italic; color: #475569;">${parseInline(quoteLines.join(' '))}</blockquote>\n`;
      } else if (/^\d+\.\s+/.test(line)) {
        if (!inList || listType !== 'ol') {
          if (inList) html += `</${listType}>\n`;
          inList = true;
          listType = 'ol';
          html += '<ol style="padding-left: 1.6rem; margin-bottom: 0.85rem; line-height: 1.65;">\n';
        }
        const itemContent = line.replace(/^\d+\.\s+/, '');
        html += `<li style="margin-bottom: 0.35rem;">${parseInline(itemContent)}</li>\n`;
      } else if (line.startsWith('- ') || line.startsWith('* ')) {
        if (!inList || listType !== 'ul') {
          if (inList) html += `</${listType}>\n`;
          inList = true;
          listType = 'ul';
          html += '<ul style="padding-left: 1.6rem; margin-bottom: 0.85rem; line-height: 1.65;">\n';
        }
        html += `<li style="margin-bottom: 0.35rem;">${parseInline(line.substring(2))}</li>\n`;
      } else {
        if (inList) { html += `</${listType}>\n`; inList = false; }
        html += `<p style="margin-bottom: 0.85rem; line-height: 1.7; text-align: justify; color: var(--text-main, #334155);">${parseInline(line)}</p>\n`;
      }
    }
    if (inList) html += `</${listType}>\n`;
    return html;
  }

  function evaluateCaseSocratic(caseData, workspace, mode) {
    const isVi = state.currentLang === 'vi';
    const pDef = (workspace.problemDefinition || '').trim();
    const evid = (workspace.evidenceObservations || '').trim();
    const stkh = (workspace.stakeholdersPerspectives || '').trim();
    const root = (workspace.rootCauseAnalysis || '').trim();
    const alts = (workspace.alternativeSolutions || '').trim();
    const crit = (workspace.evaluationCriteria || '').trim();
    const reco = (workspace.recommendation || '').trim();
    const impl = (workspace.implementationPlan || '').trim();
    const risk = (workspace.risksTradeoffs || '').trim();
    const met  = (workspace.successMetrics || '').trim();
    const note = (workspace.overallNotes || '').trim();

    const allText = [pDef, evid, stkh, root, alts, crit, reco, impl, risk, met, note].join(' ');
    const totalWords = allText ? allText.split(/\s+/).filter(Boolean).length : 0;
    const filledDims = [pDef, evid, stkh, root, alts, crit, reco, impl, risk, met].filter(t => t.length > 15).length;

    // Checks
    const hasEvidenceNumbers = /\d+/.test(evid);
    const mentionsFrontline = /nhân viên|tuyến đầu|cửa hàng|staff|employee|frontline|cashier|associate|worker/i.test(stkh + ' ' + allText);
    const mentionsTradeoffs = /rủi ro|đánh đổi|chi phí|ma sát|hạn chế|thách thức|risk|trade-off|cost|friction|downside/i.test(risk + ' ' + allText);

    // Dynamic Socratic generation
    const secA = isVi
      ? `Bài phân tích của bạn đã hoàn thành **${filledDims}/10 chiều chiến lược** với dung lượng **${totalWords} từ**. Bạn đã thể hiện tư duy có cấu trúc tốt tại phần ${reco.length > 20 ? 'Khuyến nghị giải pháp' : 'Xác định bài toán'}. Khung phân tích đi đúng trọng tâm mô hình CRM và Marketing Trải nghiệm.`
      : `Your analysis addresses **${filledDims}/10 strategic dimensions** with a total of **${totalWords} words**. Strong structural clarity is demonstrated in ${reco.length > 20 ? 'Strategic Recommendation' : 'Problem Definition'}, aligning well with foundational CRM principles.`;

    const secB = isVi
      ? (hasEvidenceNumbers
          ? `✓ **Tính xác thực cao:** Bạn đã đưa các số liệu/sự kiện thực tế vào phần Bằng chứng (${evid.substring(0, 80)}...). Việc đối chiếu số liệu định lượng giúp tách bạch rõ giữa 'Sự kiện nguồn' và 'Suy luận chủ quan'.`
          : `⚠️ **Lưu ý ranh giới Bằng chứng:** Phần Bằng chứng của bạn còn mang tính suy luận chung chung. Hãy trích dẫn thêm các số liệu thực tế từ tài liệu gốc (ví dụ: số lượng cửa hàng, tỷ lệ quy đổi voucher, chi phí đầu tư hoặc dữ liệu người dùng) để bảo vệ luận điểm vững chắc hơn.`)
      : (hasEvidenceNumbers
          ? `✓ **Strong Grounding:** You cited empirical facts/metrics in your Evidence section (${evid.substring(0, 80)}...), maintaining a clear boundary between source facts and interpretive inference.`
          : `⚠️ **Evidence Boundary Notice:** Your evidence section relies heavily on qualitative inference. Ground your claims by citing verified figures, percentages, or verbatim quotes directly from the case brief.`);

    const secC = isVi
      ? `Khi xem xét giải pháp của bạn, một số **giả định ngầm định** cần được thử thách:\n1. Bạn đang giả định khách hàng sẽ tự nhiên hào hứng đón nhận các công cụ số mới mà không gặp rào cản thay đổi thói quen.\n2. Bạn giả định hệ thống công nghệ thông tin có thể đồng bộ tức thì mà không gây tắc nghẽn dữ liệu giữa online và offline.`
      : `Critical examination of your submission reveals key **unstated assumptions**:\n1. Assuming customers will readily alter entrenched habits and download proprietary apps without friction.\n2. Assuming IT legacy infrastructure can achieve zero-latency synchronization without data silos.`;

    const secD = isVi
      ? `**Góc nhìn phản biện từ các bên:**\n- **Nhân viên tuyến đầu:** Liệu sáng kiến này có làm tăng khối lượng công việc, áp lực ca kíp hoặc yêu cầu đào tạo lại quá nặng nề không?\n- **Khách hàng bảo thủ:** Những khách hàng không rành công nghệ hoặc coi trọng sự riêng tư sẽ phản ứng ra sao khi bị buộc phải số hóa điểm chạm?`
      : `**Alternative Stakeholder Perspectives:**\n- **Frontline Employees:** Does this initiative increase task complexity, shift fatigue, or create unreasonable retraining burdens?\n- **Privacy-Sensitive Shoppers:** How will conservative or older demographics react if interpersonal warmth is replaced by digital interfaces?`;

    const secE = isVi
      ? `**Ma sát Thực thi & Đánh đổi Chiến lược:** ${mentionsTradeoffs ? 'Bạn đã có ý thức nhận diện rủi ro và sự đánh đổi.' : 'Bạn chưa phân tích sâu các sự đánh đổi không thể tránh khỏi.'} Trong quản trị CRM, cải thiện sự tiện lợi thường phải trả giá bằng chi phí đầu tư IT lớn hoặc nguy cơ mất đi trải nghiệm tiếp xúc thân mật giữa người với người (High-Touch vs High-Tech).`
      : `**Execution Friction & Strategic Trade-offs:** ${mentionsTradeoffs ? 'You correctly identified operational friction and trade-offs.' : 'You have not fully explored the unavoidable trade-offs.'} In CRM governance, frictionless speed often compromises high-touch interpersonal emotional connection or demands heavy IT capital.`;

    const devilQs = (caseData.socraticGuidance?.devil_advocate_questions) || [
      isVi ? "Nếu đối thủ sao chép 100% tính năng công nghệ này trong 6 tháng, lợi thế cạnh tranh của bạn sẽ còn lại gì?" : "If competitors clone this technological feature in 6 months, what durable moat remains?",
      isVi ? "Đâu là kịch bản xấu nhất (Worst-Case Scenario) về mặt tài chính và văn hóa nếu đề xuất này thất bại?" : "What is the worst-case financial and organizational scenario if this proposal fails?"
    ];

    const secF = isVi
      ? `**Bộ câu hỏi Socrate gợi mở:**\n1. ${devilQs[0] || ''}\n2. ${devilQs[1] || ''}`
      : `**Socratic Probing Questions:**\n1. ${devilQs[0] || ''}\n2. ${devilQs[1] || ''}`;

    const secG = isVi
      ? `**Lộ trình hoàn thiện bài phân tích:**\n1. Bổ sung ít nhất 2 chỉ số định lượng cụ thể vào phần Bằng chứng.\n2. Thêm phương án dự phòng vào phần Quản trị Rủi ro.\n3. Đối chiếu lại đề xuất với bộ câu hỏi thảo luận gốc của giáo trình.`
      : `**Actionable Refinement Roadmap:**\n1. Anchor your Evidence section with at least two quantitative metrics from the text.\n2. Detail a rollback fallback plan in Risks & Trade-offs.\n3. Compare your final synthesis against the author's original discussion questions.`;

    return {
      mode: mode,
      timestamp: new Date().toLocaleTimeString(isVi ? 'vi-VN' : 'en-US'),
      sections: {
        strengths: secA,
        evidence: secB,
        assumptions: secC,
        stakeholders: secD,
        tradeoffs: secE,
        probing: secF,
        nextSteps: secG
      }
    };
  }

  function renderCases() {
    const data = window.CRM_DATA || {};
    const casesList = data.cases || [];

    if (state.activeCaseId) {
      const activeCase = casesList.find(c => c.case_id === state.activeCaseId);
      if (activeCase) return renderCaseDetail(activeCase);
    }

    return `
      <div class="view-card">
        <div class="view-header">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 0.5rem;">
            <div>
              <h1 class="view-title">${t('cases.title')}</h1>
              <p class="view-subtitle">${t('cases.subtitle')}</p>
            </div>
            <div class="case-verified-badge">
              ✓ 10 Tình huống Nghiên cứu Thực chứng Toàn diện
            </div>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.25rem;">
          ${casesList.map(c => `
            <div style="border: 1.5px solid var(--border-color); border-radius: var(--radius-md); padding: 1.35rem; background: var(--bg-card); display: flex; flex-direction: column; justify-content: space-between; box-shadow: var(--shadow-xs); transition: all var(--transition-fast);">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                  <span style="font-size: 0.8rem; font-weight: 800; color: var(--accent-dark); text-transform: uppercase; background: var(--bg-card-subtle); padding: 0.2rem 0.5rem; border-radius: var(--radius-xs);">
                    ${c.company}
                  </span>
                  <span style="font-size: 0.75rem; color: var(--text-muted);">
                    ${c.industry}
                  </span>
                </div>
                <h3 style="color: var(--text-main); font-size: 1.15rem; margin: 0.5rem 0 0.65rem 0; line-height: 1.4;">
                  ${getText(c.title)}
                </h3>
                <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 1rem; line-height: 1.55;">
                  ${getText(c.background)}
                </p>
              </div>

              <div>
                <div style="font-size: 0.78rem; color: var(--text-soft); margin-bottom: 0.85rem; padding-top: 0.5rem; border-top: 1px dashed var(--border-subtle);">
                  📖 <strong>${c.source_reference?.document}</strong> (${c.source_reference?.chapter || ''}, pp. ${c.source_reference?.pages || ''})
                </div>
                <button class="btn btn-secondary" style="width: 100%; font-weight: 700;" onclick="window.CRM_APP.navigate('cases', '${c.case_id}')">
                  ${t('cases.viewCase')} →
                </button>
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }

  function renderCaseDetail(c) {
    const isVi = state.currentLang === 'vi';
    const cid = c.case_id;

    // Load or initialize workspace
    if (!state.progress.caseWorkspaces) state.progress.caseWorkspaces = {};
    const ws = state.progress.caseWorkspaces[cid] || {
      problemDefinition: '',
      evidenceObservations: '',
      stakeholdersPerspectives: '',
      rootCauseAnalysis: '',
      alternativeSolutions: '',
      evaluationCriteria: '',
      recommendation: '',
      implementationPlan: '',
      risksTradeoffs: '',
      successMetrics: '',
      overallNotes: state.progress.caseNotes[cid] || '',
      lastSaved: ''
    };

    const readingMode = state.caseReadingMode || 'original';
    const isModelRevealed = !!state.caseModelAnswerRevealed[cid];
    const aiFeedback = state.caseAiFeedback[cid];

    // Source texts
    const origEn = c.originalCaseText?.en || '';
    const origVi = c.originalCaseText?.vi || '';

    // Questions
    const questions = c.discussion_questions || [];
    const challenge = c.challenge_prompt;
    const fwGuide = c.frameworkGuide || {};

    const dimensionsConfig = [
      { key: 'problemDefinition', icon: '🎯', defaultTitle: isVi ? '1. Xác định Vấn đề & Bối cảnh Chiến lược' : '1. Strategic Problem & Context' },
      { key: 'evidenceObservations', icon: '📊', defaultTitle: isVi ? '2. Bằng chứng & Dữ liệu Nguồn Thực chứng' : '2. Empirical Evidence & Source Data' },
      { key: 'stakeholdersPerspectives', icon: '👥', defaultTitle: isVi ? '3. Các Bên Liên quan & Đa Góc nhìn' : '3. Stakeholders & Perspectives' },
      { key: 'rootCauseAnalysis', icon: '🔍', defaultTitle: isVi ? '4. Phân tích Nguyên nhân Gốc rễ (5 Whys)' : '4. Root Cause Analysis (5 Whys)' },
      { key: 'alternativeSolutions', icon: '💡', defaultTitle: isVi ? '5. Các Phương án Chiến lược Thay thế' : '5. Strategic Alternative Options' },
      { key: 'evaluationCriteria', icon: '⚖️', defaultTitle: isVi ? '6. Tiêu chí Đánh giá & So sánh Đánh đổi' : '6. Evaluation Criteria & Trade-offs' },
      { key: 'recommendation', icon: '🚀', defaultTitle: isVi ? '7. Khuyến nghị Giải pháp Tối ưu' : '7. Optimal Recommendation' },
      { key: 'implementationPlan', icon: '🗺️', defaultTitle: isVi ? '8. Kế hoạch Triển khai & Lộ trình Thực thi' : '8. Phased Implementation Plan' },
      { key: 'risksTradeoffs', icon: '🛡️', defaultTitle: isVi ? '9. Quản trị Rủi ro, Ma sát Vận hành & Dự phòng' : '9. Friction, Trade-offs & Mitigations' },
      { key: 'successMetrics', icon: '📈', defaultTitle: isVi ? '10. Chỉ số Đo lường Thành công (KPIs)' : '10. Success Metrics & KPIs' }
    ];

    return `
      <div class="view-card">
        <!-- Navigation Breadcrumb -->
        <div style="margin-bottom: 1.25rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
          <button class="btn btn-secondary" onclick="window.CRM_APP.clearCaseDetail()">
            ← ${isVi ? 'Danh sách tình huống' : 'Back to Case List'}
          </button>
          <div class="case-verified-badge">
            ${t('cases.sourceFidelityBadge')}
          </div>
        </div>

        <!-- Case Header -->
        <div class="case-lab-header">
          <div style="font-size: 0.85rem; font-weight: 800; color: var(--accent-dark); text-transform: uppercase; letter-spacing: 0.05em;">
            ${c.company} • ${c.industry}
          </div>
          <h1 class="view-title" style="margin-top: 0.4rem; font-size: 1.6rem;">
            ${getText(c.title)}
          </h1>
          <div class="case-source-pill">
            <span>📖 <strong>${c.source_reference?.document}</strong></span>
            <span>• ${c.source_reference?.authors || ''}</span>
            <span>• ${c.source_reference?.chapter || ''}</span>
            <span>• Trang ${c.source_reference?.pages || ''}</span>
            <span>• File: <code>${c.source_reference?.pdf_filename || ''}</code></span>
          </div>
        </div>

        <!-- Overview Context Banner -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin: 1.25rem 0 1.75rem 0;">
          <div style="background: var(--bg-card-subtle); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.15rem;">
            <h4 style="color: var(--accent-dark); margin-bottom: 0.4rem; font-size: 0.95rem;">
              🏢 ${isVi ? 'Bối cảnh Khởi đầu' : 'Business Context'}
            </h4>
            <p style="font-size: 0.9rem; color: var(--text-main); line-height: 1.55;">
              ${getText(c.background)}
            </p>
          </div>
          <div style="background: var(--pastel-yellow-light); border: 1px solid var(--pastel-yellow); border-radius: var(--radius-md); padding: 1.15rem;">
            <h4 style="color: #6B5416; margin-bottom: 0.4rem; font-size: 0.95rem;">
              🎯 ${isVi ? 'Thách thức Chiến lược' : 'Strategic Challenge'}
            </h4>
            <p style="font-size: 0.9rem; color: #4E3E11; line-height: 1.55;">
              ${getText(c.strategic_problem)}
            </p>
          </div>
        </div>

        <!-- SECTION 1: VERBATIM CASE DOCUMENT LOUNGE -->
        <div class="case-document-lounge">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem; border-bottom: 1.5px solid var(--border-subtle); padding-bottom: 0.85rem; margin-bottom: 1.25rem;">
            <div>
              <h2 style="font-size: 1.25rem; color: var(--accent-dark); margin: 0;">
                📜 ${isVi ? 'Văn bản Nghiên cứu Tình huống Gốc' : 'Verbatim Case Study Narrative'}
              </h2>
              <span style="font-size: 0.8rem; color: var(--text-muted);">
                ${t('cases.evidenceVsInferenceTip')}
              </span>
            </div>

            <!-- Reading Mode Switcher: Strictly 2 Modes (Original English & Full Vietnamese Translation) -->
            <div class="case-reading-modes">
              <button class="case-mode-btn ${readingMode === 'original' ? 'active' : ''}" onclick="window.CRM_APP.setCaseReadingMode('original')">
                ${t('cases.originalEnglish')}
              </button>
              <button class="case-mode-btn ${readingMode === 'translation' ? 'active' : ''}" onclick="window.CRM_APP.setCaseReadingMode('translation')">
                ${t('cases.vietnameseTranslation')}
              </button>
            </div>
          </div>

          <!-- Document Render Area: Single focused column with academic typography -->
          <div class="case-document-body">
            <div class="case-single-document" style="max-height: 650px; overflow-y: auto; padding-right: 0.75rem;">
              ${readingMode === 'original' ? renderCaseMarkdown(origEn) : renderCaseMarkdown(origVi)}
            </div>
          </div>

          <!-- Original Discussion Questions from Source -->
          ${questions.length > 0 ? `
            <div class="case-questions-card">
              <h3 style="color: var(--accent-dark); font-size: 1.05rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.45rem;">
                ❓ ${isVi ? 'Câu hỏi Thảo luận từ Giáo trình Gốc' : 'Original Case Discussion Questions'}
              </h3>
              ${questions.map(q => `
                <div class="case-q-item">
                  <div class="case-q-num">Câu hỏi ${q.q_num}</div>
                  <div class="case-q-text">${getText(q.prompt)}</div>
                </div>
              `).join('')}
            </div>
          ` : ''}

          <!-- CXO Challenge Card -->
          ${challenge ? `
            <div class="case-cxo-card">
              <div class="case-cxo-title">
                👑 ${t('cases.cxoChallengeBadge')}
              </div>
              <p style="font-size: 0.92rem; color: #4E3E11; line-height: 1.6;">
                ${getText(challenge.prompt)}
              </p>
            </div>
          ` : ''}
        </div>

        <!-- SECTION 2: LEARNER 10-DIMENSION WORKSPACE -->
        <div class="case-workspace-wrap">
          <div class="workspace-header-bar">
            <div>
              <h2 style="font-size: 1.3rem; color: var(--accent-dark); margin-bottom: 0.25rem;">
                ✍️ ${t('cases.workspaceTitle')}
              </h2>
              <p style="font-size: 0.85rem; color: var(--text-muted);">
                ${isVi ? 'Tự mình phân tích và hoàn thiện đề xuất trước khi mở xem gợi ý lời giải mẫu.' : 'Independently formulate your arguments across all 10 dimensions before consulting guides.'}
              </p>
            </div>

            <div class="workspace-actions">
              <span id="workspace-status" class="workspace-save-status">
                ${ws.lastSaved ? `${t('cases.autoSavedAt')} ${ws.lastSaved}` : '✓ Đã sẵn sàng'}
              </span>
              <button class="btn btn-primary" onclick="window.CRM_APP.saveCaseWorkspace('${cid}')">
                💾 ${t('cases.saveWorkspace')}
              </button>
              <button class="btn btn-secondary" onclick="window.CRM_APP.resetCaseWorkspace('${cid}')">
                ↺ ${t('cases.resetWorkspace')}
              </button>
              <button class="btn btn-secondary" onclick="window.CRM_APP.exportCaseWorkspace('${cid}')">
                📥 ${t('cases.exportReport')}
              </button>
            </div>
          </div>

          <!-- 10 Dimensions Grid -->
          <div class="dimensions-grid">
            ${dimensionsConfig.map(dim => {
              const guide = fwGuide[dim.key] || {};
              const title = getText(guide.title) || dim.defaultTitle;
              const prompt = getText(guide.prompt) || '';
              const guidelines = getText(guide.guidelines) || '';
              const val = ws[dim.key] || '';
              const wordCount = val ? val.trim().split(/\s+/).filter(Boolean).length : 0;

              return `
                <div class="dimension-card">
                  <div>
                    <div class="dim-header">
                      <div class="dim-title">${dim.icon} ${title}</div>
                    </div>
                    <div class="dim-guideline">
                      <strong>${prompt}</strong>
                      ${guidelines ? `<div style="margin-top: 0.35rem; color: var(--text-soft); font-size: 0.76rem;">${guidelines}</div>` : ''}
                    </div>
                    <textarea
                      class="dim-textarea"
                      id="dim-${dim.key}"
                      placeholder="${isVi ? 'Nhập lập luận và bằng chứng của bạn...' : 'Enter your analysis and evidence...'}"
                      oninput="window.CRM_APP.updateCaseWorkspaceField('${cid}', '${dim.key}', this.value)"
                    >${escapeHtml(val)}</textarea>
                  </div>
                  <div class="dim-footer">
                    <span>${val.length} ký tự</span>
                    <span>${wordCount} từ</span>
                  </div>
                </div>
              `;
            }).join('')}
          </div>

          <!-- Executive Summary / Overall Notes -->
          <div style="margin-top: 1.5rem; background: var(--bg-card); border: 1.5px solid var(--border-color); border-radius: var(--radius-md); padding: 1.25rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <h4 style="color: var(--accent-dark); font-size: 1rem;">
                📝 ${isVi ? 'Ghi chú & Tóm lược Điều hành (Executive Summary)' : 'Executive Summary & Overall Notes'}
              </h4>
              <span style="font-size: 0.75rem; color: var(--text-soft);">${(ws.overallNotes || '').length} ký tự</span>
            </div>
            <textarea
              class="dim-textarea"
              style="min-height: 90px;"
              placeholder="${isVi ? 'Tóm tắt thông điệp cốt lõi gửi tới Hội đồng Quản trị hoặc ghi chú cá nhân...' : 'Synthesize your executive pitch or personal study takeaways...'}"
              oninput="window.CRM_APP.updateCaseWorkspaceField('${cid}', 'overallNotes', this.value)"
            >${escapeHtml(ws.overallNotes || '')}</textarea>
          </div>
        </div>

        <!-- SECTION 3: HIDDEN MODEL ANSWERS SECTION -->
        <div class="case-model-answer-box">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
            <div>
              <h3 style="color: var(--accent-dark); font-size: 1.15rem; margin: 0;">
                🔑 ${t('cases.modelAnswerTitle')}
              </h3>
              <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0.2rem 0 0 0;">
                ${isModelRevealed ? (isVi ? 'Đang hiển thị hướng dẫn giải đối chiếu' : 'Showing comparative model answers') : t('cases.modelAnswerNotice')}
              </p>
            </div>
            <button class="btn ${isModelRevealed ? 'btn-secondary' : 'btn-primary'}" onclick="window.CRM_APP.toggleModelAnswer('${cid}')">
              ${isModelRevealed ? t('cases.hideModelAnswer') : t('cases.revealModelAnswer')}
            </button>
          </div>

          ${isModelRevealed ? `
            <div class="model-answer-content">
              <div class="model-answer-notice-banner">
                <span style="font-size: 1.25rem;">💡</span>
                <div>
                  <strong>${isVi ? 'Tài liệu tham khảo đối chiếu sư phạm:' : 'Pedagogical Reference Guide:'}</strong>
                  ${isVi
                    ? 'Không có một lời giải cứng nhắc duy nhất trong quản trị chiến lược. Các gợi ý dưới đây cung cấp hệ quy chiếu lý thuyết và bằng chứng thực tế từ tài liệu nguồn để bạn đối sánh với tư duy độc lập của mình.'
                    : 'There is no single rigid answer in strategic CRM. The following model solutions provide theoretical benchmarks and empirical source facts for comparative reflection against your independent analysis.'}
                </div>
              </div>

              ${questions.map(q => `
                <div class="model-q-answer">
                  <div style="font-weight: 700; color: var(--accent-dark); margin-bottom: 0.5rem; font-size: 0.95rem;">
                    Câu hỏi ${q.q_num}: ${getText(q.prompt)}
                  </div>
                  <div style="background: var(--bg-card-subtle); border-radius: var(--radius-sm); padding: 1rem; font-size: 0.92rem; color: var(--text-main); line-height: 1.6; border-left: 3px solid var(--accent-primary);">
                    <strong style="color: #6B5416;">${isVi ? 'Khung giải pháp & Đánh giá đối chiếu:' : 'Comparative Solution & Evaluation Rubric:'}</strong>
                    <div style="margin-top: 0.5rem;">${renderCaseMarkdown(getText(q.model_answer))}</div>
                  </div>
                </div>
              `).join('')}
            </div>
          ` : ''}
        </div>

        <!-- SECTION 4: AI SOCRATIC COACH & CRITICAL THINKING PARTNER -->
        <div class="case-ai-coach-wrap">
          <div class="ai-coach-header">
            <div class="ai-coach-avatar">🦉</div>
            <div class="ai-coach-title-block">
              <h3>${t('cases.aiCoachTitle')}</h3>
              <p>${t('cases.aiCoachSubtitle')}</p>
            </div>
          </div>

          <div class="ai-coach-toolbar">
            <button class="btn-ai-action" onclick="window.CRM_APP.triggerAiReview('${cid}', 'review')">
              ${t('cases.reviewMyAnalysis')}
            </button>
            <button class="btn-ai-action" onclick="window.CRM_APP.triggerAiReview('${cid}', 'challenge')">
              ${t('cases.challengeRecommendation')}
            </button>
            <span style="font-size: 0.8rem; color: #7C3AED; background: #F3E8FF; padding: 0.35rem 0.75rem; border-radius: var(--radius-pill); font-weight: 600;">
              ${t('cases.aiEngineLocal')}
            </span>
          </div>

          <!-- AI Feedback Render Area -->
          ${aiFeedback ? `
            <div class="ai-feedback-container">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; border-bottom: 1.5px solid #F3E8FF; padding-bottom: 0.5rem;">
                <span style="font-weight: 800; font-size: 0.95rem; color: #5B21B6;">
                  ${aiFeedback.mode === 'challenge' ? (isVi ? '⚔️ Phản biện Chiến lược & Thử thách Khuyến nghị' : '⚔️ Strategic Challenge & Devil\'s Advocacy') : (isVi ? '🔍 Kết quả Đánh giá Phản biện Socratic' : '🔍 Socratic Analysis Evaluation')}
                </span>
                <span style="font-size: 0.78rem; color: #6B7280;">
                  ${isVi ? 'Tạo lúc' : 'Generated at'}: ${aiFeedback.timestamp}
                </span>
              </div>

              <div class="socratic-section">
                <div class="socratic-sec-title">🌟 Phần A: Điểm mạnh & Điểm sáng Lập luận (Strengths)</div>
                <div class="socratic-sec-content">${renderCaseMarkdown(aiFeedback.sections.strengths)}</div>
              </div>

              <div class="socratic-section">
                <div class="socratic-sec-title">🔍 Phần B: Kiểm chứng Dữ liệu & Ranh giới Bằng chứng (Grounding)</div>
                <div class="socratic-sec-content">${renderCaseMarkdown(aiFeedback.sections.evidence)}</div>
              </div>

              <div class="socratic-section">
                <div class="socratic-sec-title">🎯 Phần C: Giả định Ngầm định & Điểm mù (Unstated Assumptions)</div>
                <div class="socratic-sec-content">${renderCaseMarkdown(aiFeedback.sections.assumptions)}</div>
              </div>

              <div class="socratic-section">
                <div class="socratic-sec-title">👥 Phần D: Góc nhìn Đối lập từ các Bên Liên quan (Stakeholders)</div>
                <div class="socratic-sec-content">${renderCaseMarkdown(aiFeedback.sections.stakeholders)}</div>
              </div>

              <div class="socratic-section">
                <div class="socratic-sec-title">⚖️ Phần E: Ma sát Thực thi & Đánh đổi Chiến lược (Trade-offs)</div>
                <div class="socratic-sec-content">${renderCaseMarkdown(aiFeedback.sections.tradeoffs)}</div>
              </div>

              <div class="socratic-section">
                <div class="socratic-sec-title">❓ Phần F: Bộ Câu hỏi Socrate để Đào sâu Tư duy (Probing Questions)</div>
                <div class="socratic-sec-content">${renderCaseMarkdown(aiFeedback.sections.probing)}</div>
              </div>

              <div class="socratic-section">
                <div class="socratic-sec-title">🚀 Phần G: Khuyến nghị Hoàn thiện Bước tiếp theo (Next Steps)</div>
                <div class="socratic-sec-content">${renderCaseMarkdown(aiFeedback.sections.nextSteps)}</div>
              </div>
            </div>
          ` : `
            <div style="background: #FFFFFF; border: 1px dashed #D8B4FE; border-radius: var(--radius-md); padding: 1.25rem; text-align: center; color: #6B7280; font-size: 0.88rem;">
              💬 ${isVi ? 'Hãy nhập các lập luận của bạn vào Không gian phân tích phía trên, sau đó nhấn nút để nhận phản biện chuyên sâu từ Cố vấn Socratic.' : 'Complete your arguments in the workspace above, then click an action button to receive rigorous Socratic coaching.'}
            </div>
          `}
        </div>
      </div>
    `;
  }

  function renderProgress() {
    const data = window.CRM_DATA || {};
    const chaptersCount = data.curriculum?.length || 0;
    const cardsCount = data.flashcards?.length || 0;
    const examsCount = data.exams?.length || 10;

    const completedChaps = state.progress.completedChapters.length;
    const completedExams = Object.keys(state.progress.examAttempts).length;
    const masteredCards = Object.values(state.progress.flashcardRatings).filter(r => r === 'easy' || r === 'good').length;

    return `
      <div class="view-card">
        <div class="view-header">
          <h1 class="view-title">${t('progress.title')}</h1>
          <p class="view-subtitle">${t('progress.subtitle')}</p>
        </div>

        <div class="stats-grid">
          <div class="stat-box">
            <div class="stat-icon">📚</div>
            <div>
              <div class="stat-number">${completedChaps} / ${chaptersCount}</div>
              <div class="stat-label">${t('progress.chaptersStudied')}</div>
            </div>
          </div>
          <div class="stat-box">
            <div class="stat-icon">🎴</div>
            <div>
              <div class="stat-number">${masteredCards} / ${cardsCount}</div>
              <div class="stat-label">${t('progress.flashcardsMastered')}</div>
            </div>
          </div>
          <div class="stat-box">
            <div class="stat-icon">📝</div>
            <div>
              <div class="stat-number">${completedExams} / ${examsCount}</div>
              <div class="stat-label">${t('progress.examsCompleted')}</div>
            </div>
          </div>
        </div>

        <div style="margin-top: 2rem;">
          <h3 style="color: var(--primary); margin-bottom: 1rem;">⚠️ ${t('progress.weakAreas')}</h3>
          <p style="color: var(--text-muted); font-size: 0.95rem;">${t('progress.noWeakAreas')}</p>
        </div>
      </div>
    `;
  }

  function renderSettings() {
    return `
      <div class="view-card">
        <div class="view-header">
          <h1 class="view-title">${t('settings.title')}</h1>
          <p class="view-subtitle">${t('settings.subtitle')}</p>
        </div>

        <div style="margin-bottom: 2rem;">
          <h3 style="color: var(--primary); margin-bottom: 0.75rem;">🌐 ${t('settings.languageSection')}</h3>
          <p style="margin-bottom: 0.75rem; font-size: 0.9rem; color: var(--text-muted);">${t('settings.currentLanguage')} <strong>${state.currentLang === 'vi' ? 'Tiếng Việt' : 'English'}</strong></p>
          <div style="display: flex; gap: 0.75rem;">
            <button class="btn ${state.currentLang === 'vi' ? 'btn-primary' : 'btn-secondary'}" onclick="window.CRM_APP.setLanguage('vi')">Tiếng Việt (Mặc định)</button>
            <button class="btn ${state.currentLang === 'en' ? 'btn-primary' : 'btn-secondary'}" onclick="window.CRM_APP.setLanguage('en')">English</button>
          </div>
        </div>

        <div style="margin-bottom: 2rem; border-top: 1px solid var(--border); padding-top: 1.5rem;">
          <h3 style="color: var(--primary); margin-bottom: 0.5rem;">💾 ${t('settings.storageSection')}</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1rem;">${t('settings.storageDesc')}</p>
          <button class="btn btn-secondary" onclick="window.CRM_APP.exportProgressData()">📥 ${t('settings.exportProgress')}</button>
        </div>

        <div style="border-top: 1px solid var(--border); padding-top: 1.5rem;">
          <h3 style="color: var(--danger); margin-bottom: 0.5rem;">⚠️ ${t('settings.resetSection')}</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1rem;">${t('settings.resetDesc')}</p>
          <button class="btn btn-danger" onclick="window.CRM_APP.resetAllProgress()">🗑️ ${t('settings.resetButton')}</button>
        </div>
      </div>
    `;
  }

  // Master Render Function
  function render() {
    const mainEl = document.getElementById('main-content');
    if (!mainEl) return;

    let html = '';
    switch (state.activeTab) {
      case 'dashboard': html = renderDashboard(); break;
      case 'library': html = renderLibrary(); break;
      case 'glossary': html = renderGlossary(); break;
      case 'flashcards': html = renderFlashcards(); break;
      case 'exams': html = renderExams(); break;
      case 'practice': html = renderPractice(); break;
      case 'cases': html = renderCases(); break;
      case 'progress': html = renderProgress(); break;
      case 'settings': html = renderSettings(); break;
      default: html = renderDashboard(); break;
    }
    mainEl.innerHTML = html;

    // Update navigation button texts based on active language
    document.querySelectorAll('[data-i18n-nav]').forEach(el => {
      const key = el.dataset.i18nNav;
      el.textContent = t(`nav.${key}`);
    });
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.dataset.i18n;
      el.textContent = t(key);
    });
  }

  // Export public API to window
  window.CRM_APP = {
    setLanguage,
    navigate,
    clearChapterDetail: () => { state.activeChapterId = null; render(); },
    toggleChapterCompleted: (chapId) => {
      const idx = state.progress.completedChapters.indexOf(chapId);
      if (idx >= 0) state.progress.completedChapters.splice(idx, 1);
      else state.progress.completedChapters.push(chapId);
      saveProgress();
      render();
    },
    setGlossarySearch: (q) => {
      state.glossarySearchQuery = q;
      render();
    },
    flipFlashcard: () => {
      state.flashcardFlipped = !state.flashcardFlipped;
      render();
    },
    nextFlashcard: () => {
      const len = window.CRM_DATA?.flashcards?.length || 1;
      state.flashcardIndex = (state.flashcardIndex + 1) % len;
      state.flashcardFlipped = false;
      render();
    },
    prevFlashcard: () => {
      const len = window.CRM_DATA?.flashcards?.length || 1;
      state.flashcardIndex = (state.flashcardIndex - 1 + len) % len;
      state.flashcardFlipped = false;
      render();
    },
    rateFlashcard: (rating) => {
      const cards = window.CRM_DATA?.flashcards || [];
      const card = cards[state.flashcardIndex];
      if (card) {
        state.progress.flashcardRatings[card.id] = rating;
        saveProgress();
      }
      window.CRM_APP.nextFlashcard();
    },
    selectExamOption: (qId, optId) => {
      if (state.examSubmitted) return; // locked after submission
      state.examAnswers[qId] = optId;
      render();
    },
    submitExam: (examId, totalQ) => {
      if (!confirm(t('exams.confirmSubmit'))) return;
      state.examSubmitted = true;
      const allQ = window.CRM_DATA?.questionBank || [];
      let score = 0;
      allQ.filter(q => q.exam_id === examId).forEach(q => {
        if (state.examAnswers[q.id] === q.correct_answer) score++;
      });
      state.progress.examAttempts[examId] = {
        score: score,
        total: totalQ,
        answers: Object.assign({}, state.examAnswers),
        date: new Date().toISOString()
      };
      saveProgress();
      render();
    },
    retakeExam: (examId) => {
      state.examSubmitted = false;
      state.examAnswers = {};
      render();
    },
    clearExamRunner: () => {
      state.activeExamId = null;
      state.examSubmitted = false;
      render();
    },
    clearCaseDetail: () => {
      state.activeCaseId = null;
      render();
    },
    setCaseReadingMode: (mode) => {
      state.caseReadingMode = mode;
      render();
    },
    updateCaseWorkspaceField: (caseId, field, val) => {
      if (!state.progress.caseWorkspaces) state.progress.caseWorkspaces = {};
      if (!state.progress.caseWorkspaces[caseId]) {
        state.progress.caseWorkspaces[caseId] = {};
      }
      state.progress.caseWorkspaces[caseId][field] = val;

      // Keep legacy caseNotes synchronized
      if (field === 'overallNotes' || (!state.progress.caseWorkspaces[caseId].overallNotes && field === 'recommendation')) {
        state.progress.caseNotes[caseId] = val;
      }

      // Debounced auto-save
      if (state.caseAutoSaveTimer) clearTimeout(state.caseAutoSaveTimer);
      state.caseAutoSaveTimer = setTimeout(() => {
        const now = new Date().toLocaleTimeString(state.currentLang === 'vi' ? 'vi-VN' : 'en-US');
        state.progress.caseWorkspaces[caseId].lastSaved = now;
        saveProgress();
        const statusEl = document.getElementById('workspace-status');
        if (statusEl) {
          statusEl.textContent = `${t('cases.autoSavedAt')} ${now}`;
        }
      }, 1000);
    },
    saveCaseWorkspace: (caseId) => {
      if (state.caseAutoSaveTimer) clearTimeout(state.caseAutoSaveTimer);
      if (!state.progress.caseWorkspaces) state.progress.caseWorkspaces = {};
      if (!state.progress.caseWorkspaces[caseId]) state.progress.caseWorkspaces[caseId] = {};
      const now = new Date().toLocaleTimeString(state.currentLang === 'vi' ? 'vi-VN' : 'en-US');
      state.progress.caseWorkspaces[caseId].lastSaved = now;
      saveProgress();
      const statusEl = document.getElementById('workspace-status');
      if (statusEl) {
        statusEl.textContent = `✓ ${t('cases.notesSaved')} (${now})`;
      } else {
        alert(t('cases.notesSaved'));
      }
    },
    resetCaseWorkspace: (caseId) => {
      if (!confirm(t('cases.resetConfirm'))) return;
      if (state.progress.caseWorkspaces && state.progress.caseWorkspaces[caseId]) {
        delete state.progress.caseWorkspaces[caseId];
      }
      delete state.progress.caseNotes[caseId];
      delete state.caseAiFeedback[caseId];
      state.caseModelAnswerRevealed[caseId] = false;
      saveProgress();
      render();
    },
    exportCaseWorkspace: (caseId) => {
      const data = window.CRM_DATA || {};
      const c = (data.cases || []).find(item => item.case_id === caseId);
      const ws = (state.progress.caseWorkspaces && state.progress.caseWorkspaces[caseId]) || {};
      const isVi = state.currentLang === 'vi';
      const title = c ? getText(c.title) : caseId;

      let md = `# BÁO CÁO PHÂN TÍCH TÌNH HUỐNG: ${title.toUpperCase()}\n`;
      md += `**Doanh nghiệp:** ${c?.company || ''} | **Ngành:** ${c?.industry || ''}\n`;
      md += `**Tài liệu Nguồn:** ${c?.source_reference?.document || ''} (${c?.source_reference?.chapter || ''}, pp. ${c?.source_reference?.pages || ''})\n`;
      md += `**Thời gian xuất:** ${new Date().toLocaleString(isVi ? 'vi-VN' : 'en-US')}\n\n`;
      md += `---\n\n## 10 Chiều Phân tích Chiến lược (Learner Analysis Framework)\n\n`;

      const dims = [
        ['1. Xác định Vấn đề & Bối cảnh', ws.problemDefinition],
        ['2. Bằng chứng & Dữ liệu Nguồn Thực chứng', ws.evidenceObservations],
        ['3. Các Bên Liên quan & Đa Góc nhìn', ws.stakeholdersPerspectives],
        ['4. Phân tích Nguyên nhân Gốc rễ (5 Whys)', ws.rootCauseAnalysis],
        ['5. Các Phương án Chiến lược Thay thế', ws.alternativeSolutions],
        ['6. Tiêu chí Đánh giá & So sánh Đánh đổi', ws.evaluationCriteria],
        ['7. Khuyến nghị Giải pháp Tối ưu', ws.recommendation],
        ['8. Kế hoạch Triển khai & Lộ trình Thực thi', ws.implementationPlan],
        ['9. Quản trị Rủi ro, Ma sát Vận hành & Dự phòng', ws.risksTradeoffs],
        ['10. Chỉ số Đo lường Thành công (KPIs)', ws.successMetrics],
        ['Ghi chú & Tóm lược Điều hành', ws.overallNotes]
      ];

      dims.forEach(([name, content]) => {
        md += `### ${name}\n${content ? content : '*(Chưa điền)*'}\n\n`;
      });

      const ai = state.caseAiFeedback[caseId];
      if (ai) {
        md += `---\n\n## Phản biện từ Cố vấn AI Socratic (Thời gian: ${ai.timestamp})\n\n`;
        md += `### Phần A: Điểm mạnh & Điểm sáng Lập luận\n${ai.sections.strengths}\n\n`;
        md += `### Phần B: Kiểm chứng Dữ liệu & Bằng chứng Nguồn\n${ai.sections.evidence}\n\n`;
        md += `### Phần C: Các Giả định Ngầm định & Điểm mù\n${ai.sections.assumptions}\n\n`;
        md += `### Phần D: Góc nhìn Đối lập từ các Bên Liên quan\n${ai.sections.stakeholders}\n\n`;
        md += `### Phần E: Ma sát Thực thi & Đánh đổi Chiến lược\n${ai.sections.tradeoffs}\n\n`;
        md += `### Phần F: Bộ Câu hỏi Socrate để Đào sâu Tư duy\n${ai.sections.probing}\n\n`;
        md += `### Phần G: Khuyến nghị Hoàn thiện Bước tiếp theo\n${ai.sections.nextSteps}\n\n`;
      }

      const blob = new Blob([md], { type: 'text/markdown;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `Case_Analysis_${caseId}_${Date.now()}.md`;
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);
    },
    toggleModelAnswer: (caseId) => {
      state.caseModelAnswerRevealed[caseId] = !state.caseModelAnswerRevealed[caseId];
      render();
    },
    triggerAiReview: (caseId, mode) => {
      const data = window.CRM_DATA || {};
      const c = (data.cases || []).find(item => item.case_id === caseId);
      if (!c) return;

      const ws = (state.progress.caseWorkspaces && state.progress.caseWorkspaces[caseId]) || {};
      const feedback = evaluateCaseSocratic(c, ws, mode);
      state.caseAiFeedback[caseId] = feedback;
      render();

      setTimeout(() => {
        const coachEl = document.querySelector('.case-ai-coach-wrap');
        if (coachEl) coachEl.scrollIntoView({ behavior: 'smooth' });
      }, 100);
    },
    saveCaseNotes: (caseId) => {
      window.CRM_APP.saveCaseWorkspace(caseId);
    },
    startRandomPractice: () => {
      const countEl = document.getElementById('practice-count');
      const diffEl = document.getElementById('practice-diff');
      const modeEl = document.getElementById('practice-mode');

      const count = parseInt(countEl?.value || '20', 10);
      const diff = diffEl?.value || 'all';
      const mode = modeEl?.value || 'instant';

      const allQ = (window.CRM_DATA?.questionBank || []).slice();
      let pool = allQ;
      if (diff !== 'all') {
        pool = allQ.filter(q => q.difficulty === diff);
      }
      if (pool.length === 0) pool = allQ;

      // Fisher-Yates shuffle
      for (let i = pool.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [pool[i], pool[j]] = [pool[j], pool[i]];
      }

      state.practiceQuestions = pool.slice(0, Math.min(count, pool.length));
      state.practiceAnswers = {};
      state.practiceSubmitted = false;
      state.practiceFeedbackMode = mode;
      render();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    },
    selectPracticeOption: (qId, optId) => {
      if (state.practiceSubmitted) return;
      if (state.practiceFeedbackMode === 'instant' && state.practiceAnswers[qId]) return; // locked after select in instant mode
      state.practiceAnswers[qId] = optId;
      render();
    },
    submitPractice: (totalQ) => {
      if (!confirm(state.currentLang === 'vi' ? 'Bạn có chắc chắn muốn nộp bài luyện tập này?' : 'Are you sure you want to submit this practice session?')) return;
      state.practiceSubmitted = true;
      render();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    },
    exitPractice: () => {
      state.practiceQuestions = [];
      state.practiceAnswers = {};
      state.practiceSubmitted = false;
      render();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    },
    exportProgressData: () => {
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(state.progress, null, 2));
      const downloadAnchor = document.createElement('a');
      downloadAnchor.setAttribute("href", dataStr);
      downloadAnchor.setAttribute("download", `crm_progress_${Date.now()}.json`);
      document.body.appendChild(downloadAnchor);
      downloadAnchor.click();
      downloadAnchor.remove();
    },
    resetAllProgress: () => {
      if (confirm(t('settings.confirmReset'))) {
        state.progress = Object.assign({}, defaultProgress);
        state.examAnswers = {};
        state.examSubmitted = false;
        saveProgress();
        render();
      }
    }
  };

  // Keyboard accessibility
  window.addEventListener('keydown', (e) => {
    if (state.activeTab === 'flashcards') {
      if (e.code === 'Space') {
        e.preventDefault();
        window.CRM_APP.flipFlashcard();
      } else if (e.code === 'ArrowRight') {
        window.CRM_APP.nextFlashcard();
      } else if (e.code === 'ArrowLeft') {
        window.CRM_APP.prevFlashcard();
      }
    }
  });

  // Mount on DOM ready
  document.addEventListener('DOMContentLoaded', () => {
    // Set initial active state on lang toggle
    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.lang === state.currentLang);
    });
    render();
  });
})();
