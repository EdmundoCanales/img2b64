# img2b64
Converts an image from different formats to base64 so it can be embeded in MarkDown.

### Example Output

![sample](tests/sample.png)

To embed this image in Markdown, use the script:

```bash
img2b64 tests/sample.png -o output.md
```

### 🧠 Option 2: Link to a Separate Markdown

Put the image snippet in a new file like `base64_snippet.md`, then:

```markdown
[▶️ View Base64-encoded image snippet](base64_snippet.md)
```
[Click here to see its embedded Base64 Markdown](tests/sampleInb64.md)