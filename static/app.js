document.getElementById('input-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const input = document.getElementById('message-input');
  const message = input.value.trim();
  if (!message) return;

  appendMessage('You', message, 'user');
  input.value = '';

  const responseElement = appendMessage('AI', '', 'assistant');
  const res = await fetch('/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message })
  });

  const reader = res.body.getReader();
  const decoder = new TextDecoder();
  let partial = '';

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    partial += decoder.decode(value);
    responseElement.textContent = `AI: ${partial}`;
  }
});

function appendMessage(sender, text, className) {
  const chat = document.getElementById('chat');
  const div = document.createElement('div');
  div.className = `message ${className}`;
  div.textContent = `${sender}: ${text}`;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
  return div;
}
