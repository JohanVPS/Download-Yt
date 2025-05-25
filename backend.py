import subprocess
from flask import Flask, request, render_template_string, redirect, url_for
import threading

app = Flask(__name__)

DOWNLOAD_FOLDER = r"C:\Users\Desktop\OneDrive\Vídeos\YoutubeMaterials\%(title)s.%(ext)s"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if not url:
            return render_template_string(INDEX_HTML, error="❌ Por favor, insira uma URL válida.")
        return redirect(url_for('download_video', url=url))
    return render_template_string(INDEX_HTML)

@app.route('/download')
def download_video():
    url = request.args.get('url')
    if not url:
        return "❌ Nenhuma URL fornecida."

    try:
        # Comando para download com qualidade máxima e saída na pasta desejada
        subprocess.run([
            'python', '-m', 'yt_dlp',
            '-f', 'bestvideo+bestaudio/best',
            '-o', DOWNLOAD_FOLDER,
            url
        ], check=True)
        
        # Página de sucesso que fecha a aba após 3 segundos
        return render_template_string(SUCCESS_HTML)
    except subprocess.CalledProcessError as e:
        return render_template_string(ERROR_HTML, error=str(e))


INDEX_HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Download YouTube</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 500px; margin: 50px auto; }
        input[type=text] { width: 100%; padding: 8px; margin: 10px 0; }
        button { padding: 10px 20px; }
        .error { color: red; }
    </style>
</head>
<body>
    <h2>Baixar vídeo do YouTube</h2>
    {% if error %}
        <p class="error">{{ error }}</p>
    {% endif %}
    <form method="post">
        <input type="text" name="url" placeholder="Cole o link do vídeo aqui" required>
        <button type="submit">Baixar</button>
    </form>
</body>
</html>
'''

SUCCESS_HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Download Concluído</title>
    <script>
        // Fecha a aba após 3 segundos
        setTimeout(() => { window.close(); }, 3000);
    </script>
</head>
<body style="font-family: Arial, sans-serif; max-width: 500px; margin: 50px auto; text-align:center;">
    <h2>✅ Download concluído com sucesso!</h2>
    <p>A aba fechará automaticamente em 3 segundos.</p>
</body>
</html>
'''

ERROR_HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Erro no Download</title>
    <style> body { font-family: Arial, sans-serif; max-width: 500px; margin: 50px auto; color: red; } </style>
</head>
<body>
    <h2>❌ Erro ao baixar o vídeo</h2>
    <p>{{ error }}</p>
    <a href="/">Voltar</a>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
