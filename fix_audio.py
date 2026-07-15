import re

with open('index.html', 'r') as f:
    content = f.read()

# Fix the audio element - remove trailing space and update comment
content = content.replace(
    '<!-- Audio element for streaming (HTTP because the SSL cert on the stream server has expired) -->',
    '<!-- Audio element for streaming (no crossorigin to avoid CORS blocks - stream server lacks proper headers) -->'
)
content = content.replace(
    '<audio id="audioPlayer" preload="none" >',
    '<audio id="audioPlayer" preload="none">'
)

with open('index.html', 'w') as f:
    f.write(content)

print("Fix applied successfully")