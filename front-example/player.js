function secondsToMinutesAndSeconds(seconds) {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
}

function textColorOnBackground(rgb) {
    var r = rgb[0] / 255;
    var g = rgb[1] / 255;
    var b = rgb[2] / 255;
    if (0.2126 * r + 0.7152 * g + 0.0722 * b > 0.5) {
        return 'black';
    } else {
        return 'white';
    }
}

function fetchDataAndAnimate() {
    fetch('https://api.noh.am/music/get') // récupère les données depuis l'API
        .then(response => response.json())
        .then(data => {
            const artist = data.artist;
            const album = data.album;
            const artist_url = data.artist_url;
            const artwork_url = data.artwork_url;
            const time = data.time;
            const itunes_url = data.itunes_url;
            const name = data.name;
            const timestamp = parseFloat(data.timestamp);
            const decalage = (Date.now() / 1000 - timestamp);
            let pPosition = Math.round(parseFloat(data.pPosition) + decalage - 3);
            const duration = parseFloat(data.duration);
            const status = data.status;
            const dominantcolor = data.dominantcolor;
            const textColor = textColorOnBackground(dominantcolor);
            
            const lastTime = document.querySelector('.last-time');
            lastTime.style.color = textColor;
            const totalTime = document.querySelector('.total-time');
            totalTime.style.color = textColor;

            const titleSongElement = document.querySelector('.title-song');
            titleSongElement.textContent = `${name} - `
            titleSongElement.style.color = textColor;

            const titleAlbumElement = document.querySelector('.title-album');
            titleAlbumElement.textContent = album;
            titleAlbumElement.style.color = textColor;

            const artistSongElement = document.querySelector('.name-artist');
            artistSongElement.textContent = artist;
            artistSongElement.style.color = textColor;

            const artworkElement = document.querySelector('.artwork_url');
            artworkElement.src = artwork_url;

            const playerDiv = document.querySelector('.player');
            const colorString = 'rgb(' + dominantcolor.join(',') + ')';
            playerDiv.style.backgroundColor = colorString;

            const artist_urlElement = document.querySelector('.artist-url');
            artist_urlElement.href = artist_url;

            const songUrlElements = document.querySelectorAll('.song-url');
            songUrlElements.forEach(element => {
                element.href = itunes_url;
            });

            if (status === 'playing' && (pPosition / duration) * 100 <= 100) { // actualise une première fois
                const totaltimeElement = document.querySelector('.total-time');
                totaltimeElement.textContent = time;

                const lasttimeElement = document.querySelector('.last-time');
                lasttimeElement.textContent = secondsToMinutesAndSeconds(pPosition);

                const rapport = (pPosition / duration) * 100;
                const trackElements = document.querySelectorAll('.track');
                trackElements.forEach(element => {
                    const style = window.getComputedStyle(element, '::after');
                    const currentWidth = parseFloat(style.getPropertyValue('width'));
                    element.style.setProperty('--new-width', `${rapport.toFixed(2)}%`);
                    element.style.setProperty('--new-color', textColor);
                });

                let intervalId;

                function updateProgress() {
                    const lasttimeElement = document.querySelector('.last-time');
                    lasttimeElement.textContent = secondsToMinutesAndSeconds(pPosition);
                    const rapport = (pPosition / duration) * 100;
                    const trackElements = document.querySelectorAll('.track');
                    trackElements.forEach(element => {
                        element.style.setProperty('--new-width', `${rapport.toFixed(2)}%`);
                        element.style.setProperty('--new-color', textColor);
                    });
                    pPosition++;
                    if (pPosition > duration) {
                        clearInterval(intervalId);
                        fetchDataAndAnimate();
                    }
                }

                intervalId = setInterval(updateProgress, 1000); // actualise le compteur toutes les secondes
            }
            else { // si le lecteur ne joue rien alors il affiche la dernière musique jouée
                const totaltimeElement = document.querySelector('.total-time');
                totaltimeElement.textContent = time;

                const lasttimeElement = document.querySelector('.last-time');
                lasttimeElement.textContent = time;

                const rapport = (pPosition / duration) * 100;
                const trackElements = document.querySelectorAll('.track');
                trackElements.forEach(element => {
                    const style = window.getComputedStyle(element, '::after');
                    const currentWidth = parseFloat(style.getPropertyValue('width'));
                    element.style.setProperty('--new-width', `100%`);
                    element.style.setProperty('--new-color', textColor);
                });
            }
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

fetchDataAndAnimate();