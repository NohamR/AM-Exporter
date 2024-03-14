function secondsToMinutesAndSeconds(seconds) {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
}
function fetchDataAndAnimate() {
    // fetch('http://192.168.1.58:3005/music/get')
    fetch('https://api.noh.am/music/get')
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

            const titleSongElement = document.querySelector('.title-song');
            // titleSongElement.textContent = name;
            titleSongElement.textContent = `${name} - `

            const titleAlbumElement = document.querySelector('.title-album');
            titleAlbumElement.textContent = album;

            const artistSongElement = document.querySelector('.name-artist');
            artistSongElement.textContent = artist;

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

            if (status === 'playing' && (pPosition / duration) * 100 <= 100) {
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
                });

                let intervalId;

                function updateProgress() {
                    const lasttimeElement = document.querySelector('.last-time');
                    lasttimeElement.textContent = secondsToMinutesAndSeconds(pPosition);
                    const rapport = (pPosition / duration) * 100;
                    const trackElements = document.querySelectorAll('.track');
                    trackElements.forEach(element => {
                        element.style.setProperty('--new-width', `${rapport.toFixed(2)}%`);
                    });
                    pPosition++;
                    if (pPosition > duration) {
                        clearInterval(intervalId);
                        fetchDataAndAnimate();
                    }
                }

                intervalId = setInterval(updateProgress, 1000);
            }
            else {
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
                });
            }
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

fetchDataAndAnimate();