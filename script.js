(function() {
    // Pega a URL do vídeo atual
    const videoUrl = window.location.href;

    // Verifica se é uma página de vídeo do YouTube
    if (!videoUrl.includes("watch?v=")) {
        alert("Este script só funciona em páginas de vídeo do YouTube.");
        return;
    }

    // URL da API ou do backend que faz o download (substitua se for o caso)
    const apiUrl = "http://localhost:5000/download?url=" + encodeURIComponent(videoUrl);

    // Abre uma nova aba com o backend (opcional) ou envia requisição
    window.open(apiUrl, "_blank");

    // Alternativa: copiar o link para a área de transferência
    navigator.clipboard.writeText(videoUrl).then(() => {
        console.log("Link copiado para a área de transferência:", videoUrl);
        alert("Link copiado! Agora use seu downloader externo.");
    });
})();
