# CONTENT CLASSIFICATION CRITERIA - AI AGENT DETERMINISTIC RULES

## META-INSTRUCTIONS
**TARGET**: Claude AI Sonnet 4.5 content classification
**AUTHORITY**: This document is NORMATIVE for content placement decisions
**PRIORITY**: Deterministic, zero-ambiguity, binary decisions
**LANGUAGE**: English (criteria apply to multilingual content)

---

## CLASSIFICATION ALGORITHM

```python
def classify_content(text_chunk):
    """
    Process content through decision tree.
    First match wins. Order matters.
    """

    # PRIORITY 1: Format-based (unambiguous)
    if has_explicit_tradeoff_markers(text_chunk):
        return "tradeoffs/"

    if has_tabular_structure(text_chunk):
        if is_chart_data(text_chunk):
            return "data/"
        else:
            return "tables/"

    if is_question_answer_pair(text_chunk):
        return "faqs/"

    if is_graph_notation(text_chunk):
        return "diagrams/"

    # PRIORITY 2: Semantic markers (explicit)
    if has_legal_disclaimer_markers(text_chunk):
        return "disclaimers/"

    if has_callout_markers(text_chunk):
        return "callouts/"

    if has_dock_markers(text_chunk):
        return "docks/"

    # PRIORITY 3: Default categories
    if is_flowing_prose(text_chunk):
        return "plaintext/"

    # FALLBACK
    return "others/"
```

---

## CATEGORY 1: tradeoffs/

### DETERMINISTIC CRITERIA (MUST MATCH ALL)

```yaml
REQUIRED_FORMAT:
  - Each line starts with EXACTLY "+" or "-" (no spaces before)
  - Minimum 2 lines (at least 1 pro AND 1 con preferred, but 2 of same type allowed)
  - Each line has text after the marker
  - No mixing with other content types

REGEX_PATTERN: ^[+-]\s+.+$

POSITIVE_EXAMPLES:
  ✓ "+ Claritas superfluitatem vincit"
  ✓ "- Ornamentum sine utilitate tardat"
  ✓ "+ Benefit one\n+ Benefit two\n- Drawback one"

NEGATIVE_EXAMPLES:
  ✗ "Pros: benefit"              # No + marker
  ✗ " + benefit"                 # Space before marker
  ✗ "+benefit"                   # No space after marker
  ✗ "Advantages and disadvantages" # Prose format
```

### BINARY TEST
```python
def is_tradeoff(text):
    lines = text.strip().split('\n')
    if len(lines) < 2:
        return False

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if not (line.startswith('+ ') or line.startswith('- ')):
            return False

    return True
```

---

## CATEGORY 2: tables/

### DETERMINISTIC CRITERIA (MUST MATCH ALL)

```yaml
REQUIRED_FORMAT:
  - Contains tab character (\t) as separator
  - Minimum 2 lines (header + 1 data row)
  - First line is header row
  - All rows have SAME number of columns
  - Primary purpose: display as visual table
  - NOT intended for chart/graph rendering

COLUMN_COUNT: uniform across all rows
SEPARATOR: \t (tab character, ASCII 0x09)

POSITIVE_EXAMPLES:
  ✓ "Column1\tColumn2\tColumn3\nValue1\tValue2\tValue3"
  ✓ "Name\tAge\tCity\nJohn\t30\tNY\nJane\t25\tLA"

NEGATIVE_EXAMPLES:
  ✗ "Column1,Column2"             # CSV (comma-separated)
  ✗ "Column1  Column2"            # Space-separated
  ✗ "Year\tValue"                 # Only header, no data (unless placeholder)
  ✗ "Name\tAge\nJohn\t30\t50"    # Inconsistent columns
```

### BINARY TEST
```python
def is_table(text):
    lines = text.strip().split('\n')
    if len(lines) < 2:
        return False

    if '\t' not in text:
        return False

    header_cols = len(lines[0].split('\t'))
    for line in lines[1:]:
        if len(line.split('\t')) != header_cols:
            return False

    # Not a chart data pattern
    if is_chart_data(text):
        return False

    return True
```

---

## CATEGORY 3: data/

### DETERMINISTIC CRITERIA (MUST MATCH ALL)

```yaml
REQUIRED_FORMAT:
  - TSV format (tab-separated)
  - Minimum 2 lines (header + 1 data row)
  - Primary purpose: feed chart/graph visualization
  - Typical patterns:
    - Time series: Year/Month/Date column + numeric values
    - Categorical: Category column + numeric values
    - Multi-series: Category + multiple numeric columns

INDICATORS:
  - Column names suggest metrics: "Value", "Count", "Amount", "Total", "Percentage"
  - Column names suggest time: "Year", "Month", "Date", "Period"
  - Data is primarily numeric (except category column)
  - Suitable for line/bar/pie charts

POSITIVE_EXAMPLES:
  ✓ "Year\tSales\n2023\t1000\n2024\t1500"
  ✓ "Month\tRevenue\tProfit\nJan\t100\t20\nFeb\t150\t30"
  ✓ "Category\tPercentage\nA\t45\nB\t55"

NEGATIVE_EXAMPLES:
  ✗ "Name\tEmail\tPhone"          # Contact list (not chart data)
  ✗ "Product\tDescription\tPrice" # Product catalog (not metric-focused)
```

### BINARY TEST
```python
def is_chart_data(text):
    if not is_table(text):
        return False

    lines = text.strip().split('\n')
    header = lines[0].split('\t')

    # Check for metric/time indicators in header
    metric_keywords = ['value', 'count', 'amount', 'total', 'percentage',
                       'sales', 'revenue', 'profit', 'year', 'month', 'date']

    header_lower = ' '.join(header).lower()
    if any(kw in header_lower for kw in metric_keywords):
        return True

    # Check if data rows are primarily numeric
    numeric_cols = 0
    for i, col in enumerate(header):
        if i == 0:  # First column can be category
            continue
        is_numeric = True
        for line in lines[1:]:
            value = line.split('\t')[i]
            try:
                float(value.replace(',', '.'))
            except:
                is_numeric = False
                break
        if is_numeric:
            numeric_cols += 1

    return numeric_cols >= 1
```

---

## CATEGORY 4: faqs/

### DETERMINISTIC CRITERIA (MUST MATCH ALL)

```yaml
REQUIRED_FORMAT:
  - Two distinct parts: Question + Answer
  - Question ends with "?" OR starts with interrogative word
  - Answer is separate paragraph/section
  - Typical markers:
    - "Q:", "A:" labels
    - "Question:", "Answer:" labels
    - Numbered Q&A format
    - Clear question sentence + response

INTERROGATIVE_STARTERS:
  - What, Why, How, When, Where, Who, Which, Can, Could, Should, Would, Is, Are, Does, Do

POSITIVE_EXAMPLES:
  ✓ "Q: What is this?\nA: This is an answer."
  ✓ "Question: How does it work?\nAnswer: It works by..."
  ✓ "Why is this important?\n\nBecause it provides value."
  ✓ "Can I use this?\nYes, you can."

NEGATIVE_EXAMPLES:
  ✗ "This is a statement."        # No question
  ✗ "What is this?"               # Question only, no answer
  ✗ "The answer is 42."           # Answer only, no question
```

### BINARY TEST
```python
def is_faq(text):
    # Check for explicit Q:/A: format
    if ('Q:' in text or 'Question:' in text) and ('A:' in text or 'Answer:' in text):
        return True

    # Check for question + answer pattern
    sentences = text.split('\n\n')
    if len(sentences) < 2:
        sentences = text.split('. ')

    has_question = False
    has_answer = False

    interrogatives = ['what', 'why', 'how', 'when', 'where', 'who', 'which',
                      'can', 'could', 'should', 'would', 'is', 'are', 'does', 'do']

    for sent in sentences:
        sent_lower = sent.lower().strip()
        if sent.strip().endswith('?'):
            has_question = True
        elif any(sent_lower.startswith(q) for q in interrogatives):
            if '?' in sent:
                has_question = True
        elif has_question and len(sent.strip()) > 20:
            has_answer = True

    return has_question and has_answer
```

---

## CATEGORY 5: diagrams/

### DETERMINISTIC CRITERIA (MUST MATCH ALL)

```yaml
REQUIRED_FORMAT:
  - Contains Graphviz DOT syntax
  - Starts with "digraph" or "graph" keyword
  - Contains node/edge definitions with "->" or "--"
  - Enclosed in curly braces

DOT_KEYWORDS: digraph, graph, node, edge, rankdir, label

POSITIVE_EXAMPLES:
  ✓ "digraph G { A -> B; }"
  ✓ "graph G { A -- B; }"
  ✓ "digraph Flow { rankdir=LR; Start -> Process -> End; }"

NEGATIVE_EXAMPLES:
  ✗ "Process flow: Start -> End"  # Prose, not DOT syntax
  ✗ "A connects to B"             # Description, not diagram code
  ✗ "[A] -> [B]"                  # Similar but not DOT
```

### BINARY TEST
```python
def is_diagram(text):
    text_lower = text.lower().strip()

    # Must contain digraph or graph
    if not ('digraph' in text_lower or 'graph' in text_lower):
        return False

    # Must have curly braces
    if '{' not in text or '}' not in text:
        return False

    # Must have edge operator
    if not ('->' in text or '--' in text):
        return False

    return True
```

---

## CATEGORY 6: disclaimers/

### DETERMINISTIC CRITERIA (MUST MATCH ALL)

```yaml
REQUIRED_CONTENT:
  - Contains legal/risk/warning language
  - Typical markers (case-insensitive):
    - "disclaimer", "warning", "caution", "notice", "important"
    - "not responsible", "no warranty", "no guarantee"
    - "at your own risk", "use at your own risk"
    - "consult", "legal advice", "professional advice"
    - "terms and conditions", "subject to change"

TONE: Formal, protective, limiting liability

POSITIVE_EXAMPLES:
  ✓ "Disclaimer: This information is provided as-is without warranty."
  ✓ "Warning: Use at your own risk. Consult a professional."
  ✓ "Important: No guarantee of accuracy. Subject to change."
  ✓ "Cave ne interpretatio excedat voluntatem textus." (Legal warning in Latin)

NEGATIVE_EXAMPLES:
  ✗ "Please note that this is useful."  # Note, but not disclaimer
  ✗ "Remember to save your work."       # Reminder, not legal warning
```

### BINARY TEST
```python
def is_disclaimer(text):
    text_lower = text.lower()

    disclaimer_markers = [
        'disclaimer', 'warning', 'caution', 'notice',
        'not responsible', 'no warranty', 'no guarantee',
        'at your own risk', 'use at your own risk',
        'consult', 'legal advice', 'professional advice',
        'terms and conditions', 'subject to change',
        'cave', 'monitum', 'cautio'  # Latin legal terms
    ]

    marker_count = sum(1 for marker in disclaimer_markers if marker in text_lower)

    # Require at least 2 markers for high confidence
    return marker_count >= 2 or (marker_count >= 1 and len(text.split()) < 50)
```

---

## CATEGORY 7: callouts/

### DETERMINISTIC CRITERIA (MUST MATCH ALL)

```yaml
REQUIRED_CHARACTERISTICS:
  - Short, attention-grabbing message (typically < 200 words)
  - Highlights key point, tip, or important information
  - Often contains markers:
    - "Note:", "Tip:", "Info:", "Important:", "Remember:"
    - Emoji/symbols (optional): ℹ️, ⚠️, 💡, ✓, 🔔
    - ALL CAPS words (emphasis)
  - Standalone message (not part of flowing narrative)
  - Would be visually highlighted in UI

TYPICAL_PREFIXES: Note, Tip, Info, Important, Remember, Key Point, Heads Up

POSITIVE_EXAMPLES:
  ✓ "Note: Always backup your data before proceeding."
  ✓ "Tip: Use keyboard shortcuts to work faster."
  ✓ "IMPORTANT: Read all instructions carefully."
  ✓ "Remember: Save your progress frequently."

NEGATIVE_EXAMPLES:
  ✗ "This paragraph explains the concept in detail..." # Too long, flowing
  ✗ "The next step is to configure settings."         # Part of sequence
```

### BINARY TEST
```python
def is_callout(text):
    text_stripped = text.strip()

    # Length check (short messages)
    word_count = len(text_stripped.split())
    if word_count > 200:
        return False

    # Check for explicit markers
    callout_markers = ['note:', 'tip:', 'info:', 'important:', 'remember:',
                       'key point:', 'heads up:', 'warning:', 'attention:']

    text_lower = text_stripped.lower()
    if any(text_lower.startswith(marker) for marker in callout_markers):
        return True

    # Check for ALL CAPS emphasis
    words = text_stripped.split()
    caps_words = [w for w in words if w.isupper() and len(w) > 3]
    if len(caps_words) >= 2 and word_count < 50:
        return True

    return False
```

---

## CATEGORY 8: docks/

### DETERMINISTIC CRITERIA (MUST MATCH ALL)

```yaml
REQUIRED_CHARACTERISTICS:
  - Editorial side note or supplementary information
  - Not essential to main narrative
  - Provides context, background, or related information
  - Typical markers:
    - "Note:", "Side note:", "Background:", "Context:", "FYI:"
    - "See also:", "Related:", "More info:", "Additional:"
    - References to external resources
  - Would appear in sidebar or margin in UI

DISTINGUISHES_FROM_CALLOUT:
  - Longer than callout (100-500 words typical)
  - Informational rather than attention-grabbing
  - Optional reading, not critical alert

POSITIVE_EXAMPLES:
  ✓ "Background: This concept originated in the 1970s..."
  ✓ "Side note: For more details, see the appendix."
  ✓ "Context: In Latin tradition, this practice was common."
  ✓ "FYI: The terminology varies by region."

NEGATIVE_EXAMPLES:
  ✗ "IMPORTANT: You must do this now."  # Callout (urgent)
  ✗ "The main point is..."              # Main content (plaintext)
```

### BINARY TEST
```python
def is_dock(text):
    text_stripped = text.strip()
    word_count = len(text_stripped.split())

    # Length range (longer than callout, shorter than full article)
    if word_count < 20 or word_count > 500:
        return False

    # Check for dock markers
    dock_markers = ['background:', 'side note:', 'context:', 'fyi:',
                    'see also:', 'related:', 'more info:', 'additional:',
                    'nota:', 'contextus:']  # Latin variants

    text_lower = text_stripped.lower()
    if any(text_lower.startswith(marker) for marker in dock_markers):
        return True

    # Check for reference patterns
    reference_patterns = ['see ', 'refer to', 'consult', 'for more', 'additional information']
    if any(pattern in text_lower for pattern in reference_patterns):
        if word_count >= 50:
            return True

    return False
```

---

## CATEGORY 9: plaintext/

### DETERMINISTIC CRITERIA (DEFAULT CATEGORY)

```yaml
REQUIRED_CHARACTERISTICS:
  - Flowing prose or narrative text
  - No special formatting markers
  - Main content body
  - Typically > 50 words
  - Paragraphs of sentences
  - Would fill main content area in UI

TYPICAL_CONTENT:
  - Article sections
  - Explanatory text
  - Narrative descriptions
  - Educational content
  - Standard paragraphs

POSITIVE_EXAMPLES:
  ✓ "Lorem ipsum dolor sit amet, consectetur adipiscing elit..."
  ✓ "This section explains the fundamental concepts of..."
  ✓ "In the context of ethics, we must consider..."

NEGATIVE_EXAMPLES:
  ✗ (Anything matching other categories above)
```

### BINARY TEST
```python
def is_plaintext(text):
    # Default category if no other category matches

    # Minimum length
    if len(text.strip().split()) < 20:
        return False

    # Check it's not another category
    if (is_tradeoff(text) or is_table(text) or is_chart_data(text) or
        is_faq(text) or is_diagram(text) or is_disclaimer(text) or
        is_callout(text) or is_dock(text)):
        return False

    return True
```

---

## CATEGORY 10: others/

### DETERMINISTIC CRITERIA (FALLBACK)

```yaml
REQUIRED_CHARACTERISTICS:
  - Does not fit any other category
  - Miscellaneous textual content
  - Edge cases
  - Fragments
  - Lists without +/- markers
  - Short notes
  - Anything ambiguous

USE_CASES:
  - Bullet lists (without +/-)
  - Numbered lists
  - Short fragments (< 20 words)
  - Mixed content that doesn't cleanly categorize
  - Temporary/placeholder content

POSITIVE_EXAMPLES:
  ✓ "• Item one\n• Item two\n• Item three"
  ✓ "1. First\n2. Second\n3. Third"
  ✓ "Short note."
  ✓ "TODO: Add content here"

NEGATIVE_EXAMPLES:
  ✗ (Anything clearly matching other categories)
```

### BINARY TEST
```python
def is_other(text):
    # Fallback category - always returns True if reached
    return True
```

---

## DECISION TREE EXECUTION ORDER

```
1. Is tradeoff format (+/-)? → tradeoffs/
2. Is TSV table format?
   a. Is chart data? → data/
   b. Else → tables/
3. Is FAQ format (Q&A)? → faqs/
4. Is DOT diagram? → diagrams/
5. Is legal disclaimer? → disclaimers/
6. Is callout (short, attention)? → callouts/
7. Is dock (side note, context)? → docks/
8. Is plaintext (flowing prose)? → plaintext/
9. FALLBACK → others/
```

---

## MULTI-CATEGORY RESOLUTION

```yaml
IF multiple categories match:
  PRIORITY_ORDER:
    1. tradeoffs/     # Format is unambiguous
    2. tables/        # Format is unambiguous
    3. data/          # Format is unambiguous
    4. faqs/          # Format is unambiguous
    5. diagrams/      # Format is unambiguous
    6. disclaimers/   # Semantic marker
    7. callouts/      # Semantic marker
    8. docks/         # Semantic marker
    9. plaintext/     # Default prose
    10. others/       # Fallback

MULTI_CHOICE_SCENARIOS:
  - If text could be callout OR dock:
    → Check length: < 100 words = callout, >= 100 words = dock

  - If text could be plaintext OR dock:
    → Check markers: has markers = dock, no markers = plaintext

  - If text could be disclaimer OR callout:
    → Check legal language: legal = disclaimer, emphasis = callout

PRESENT_TO_USER:
  - If confidence < 80%, show multiple options
  - Format: "Primary: X (80%), Secondary: Y (15%), Other: Z (5%)"
```

---

## EDGE CASES

```yaml
EMPTY_TEXT:
  → REJECT (require minimum content)

SINGLE_WORD:
  → others/

MIXED_LANGUAGES:
  → Apply same criteria (language-agnostic where possible)

CODE_SNIPPETS:
  → others/ (unless it's DOT diagram code)

POETRY/VERSE:
  → plaintext/ (treat as prose)

QUOTATIONS:
  → plaintext/ or docks/ (depends on context/markers)

DEFINITIONS:
  → docks/ if marked "Definition:", else plaintext/
```

---

## OUTPUT FORMAT FOR CLASSIFICATION

```yaml
CLASSIFICATION_RESULT:
  primary_category: "category-name/"
  confidence: 0.95
  reasoning: "Text contains +/- markers on each line, matches tradeoff format"
  alternatives:
    - category: "others/"
      confidence: 0.05
      reasoning: "Could be general list"

  filename_suggestion: "descriptive-slug-name.txt"
  validation_passed: true
  warnings: []
```

---

## VERSION HISTORY

- v1.0.0 (2025-11-12): Initial deterministic classification criteria

---

**END OF CLASSIFICATION CRITERIA - NORMATIVE FOR CONTENT INGESTION**
