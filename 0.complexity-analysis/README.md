GitHub uses Markdown (often referred to as GitHub Flavored Markdown or GFM) for formatting text in issues, pull requests, comments, and readme files.  
A guide on how to write basic Markdown for GitHub:

1. Headings:

Markdown provides six levels of headings, from H1 to H6.

# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

2. Paragraphs and Line Breaks:

    A paragraph is simply a block of text with a blank line before and after it.
    For a line break (new line within the same paragraph), use two spaces at the end of a line and press enter.

This is a paragraph.

This is another paragraph.

For line breaks:

This is a line.  
This is the next line.

3. Bold and Italic Text:

    Bold: Wrap text in two asterisks (**) or underscores (__).
    Italic: Wrap text in one asterisk (*) or one underscore (_).
    Bold and Italic: Use three asterisks (***).

**Bold text**

*Italic text*

***Bold and italic text***

4. Lists:

    Unordered List: Use -, *, or + for list items.
    Ordered List: Use numbers followed by a period.

- Item 1
- Item 2
  - Sub-item 1
  - Sub-item 2

1. First item
2. Second item
3. Third item

5. Links:

To create a link, use the format [text](URL).

[GitHub](https://github.com)

For a link that opens in a new tab (for certain contexts), you can use HTML:

<a href="https://github.com" target="_blank">GitHub</a>

6. Images:

The syntax for images is similar to links but with an exclamation mark (!) in front:

![Alt text](URL_of_image)

Example:

![GitHub Logo](https://github.com/favicon.ico)

7. Code:

    Inline Code: Use backticks (`) to wrap inline code.
    Code Blocks: Use triple backticks (```) to create code blocks. You can specify the language for syntax highlighting.

`inline code`

```python
def hello_world():
    print("Hello, world!")


### 8. **Blockquotes:**

To create a blockquote, use the greater-than sign (`>`).

```markdown
> This is a blockquote.

9. Horizontal Rule:

A horizontal rule (a line) can be created using three dashes (---), three asterisks (***), or three underscores (___).

---

10. Tables:

To create tables, use pipes (|) and dashes (-).

| Header 1 | Header 2 |
|----------|----------|
| Row 1    | Data 1   |
| Row 2    | Data 2   |

11. Task Lists:

GitHub supports task lists (checkboxes) for issues and pull requests.

- [x] Completed task
- [ ] Incomplete task

12. Mentioning Users and Repositories:

You can mention users, teams, and repositories using @username, @org/team, and owner/repository.

@octocat mentioned you in an issue.

13. Emoji:

GitHub supports emoji syntax. Use :emoji_name: to include emojis.

:smile: :heart: :octocat:

14. Syntax Highlighting in Code Blocks:

To specify a language for syntax highlighting in a code block, place the language name directly after the opening triple backticks.

```javascript
console.log("Hello, world!");


### 15. **HTML in Markdown:**

You can use HTML tags directly in Markdown for more control over your formatting.

```markdown
<p>This is HTML inside Markdown.</p>

---
# Difference between basic markdown and GFM

Basic Markdown (such as headings, lists, bold, italics, code, etc.) is standardized, so the same syntax should work across any platform that supports Markdown.

    - Headings: # Heading 1, ## Heading 2, etc.
    - Bold: **bold text**
    - Italic: *italic text*
    - Code: Inline with backticks: `code`, and blocks with triple backticks.

GitHub Flavored Markdown (GFM) includes extra features specific to GitHub. These features may not work exactly the same (or at all) on other platforms unless they also support them. These extra features include:

    - Task Lists: - [ ] and - [x] for checkboxes (specific to GitHub Issues, PRs, etc.).
    - Mentions: @username to mention users or teams.
    - Tables: While tables work in basic Markdown, GFM makes it easier and more consistent.
    - Emoji: GitHub supports emoji syntax like :smile:.
    - Autolinks: URLs automatically become clickable (e.g., http://example.com becomes a clickable link).
    - Rendering of @mentions and repository references (e.g., owner/repository).