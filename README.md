# AppleMusicExporter

AppleMusicExporter est un projet conçu pour exporter les musiques depuis Apple Music en temps réel. AppleMusicExporter utilise [AppleScript](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html) pour les interactions avec Apple Music.

<img src="Diagramme.drawio.png" width="800" height="437"/> <!-- 781 × 437 -->

## Dépendances :

### Back :
 - flask
 - python-dotenv (optionnel)
 - requests

### User :
 - colorthief
 - python-dotenv
 - requests

## Install :
### Back :
```bash
git clone https://github.com/NohamR/AM-Exporter.git
cd back
```
Créer le fichier .users avec les utilisateurs et leurs mots de passe hashés ([.user.example](back/.users.example)).
```bash  
docker build -t amexporter .
```
```bash
docker run -d -p 3005:3005 amexporter
```
Ou 
```bash
docker-compose up -d
```

### User :
```bash
git clone https://github.com/NohamR/AM-Exporter.git
cd user
python install -r requirements.txt
```
Créer le fichier .env avec l'utilisateur et son mot de passe ([.env.example](user/.env.example)).

Configuer [music-exp.plist](user/music-exp.plist) sur l'exemple de [music-exp.plist.example](user/music-exp.plist.example) :
PYTHON_PATH
WORKING_DIRECTORY
```bash
./install.sh
```
![notif.png](notif.png)

Logs can but found in the working direcrtory :
```bash
cd WORKING_DIRECTORY
tail -f error_logfile.log
tail -f logfile.log
```

### Front :
Un exemple d'implémentation de l'api est disponible dans [front-example](front-example) :
<!-- ![screen.png](front-example/screen.png) -->
<img src="front-example/screen.png" width="400" height="331"/> <!-- 710 × 588 -->
<img src="Music-Player.gif" width="400" height="331"/>

## Uninstall :
```bash
cd user
./unistall.sh
```

# To do :
- comment