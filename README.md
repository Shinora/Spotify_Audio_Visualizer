# Spotify_Audio_Visualizer

Pour faire fonctionner le script, il faut aller sur le dashboard developpeur spotify et créer une app. 
Notez votre id client et votre id client secret, ils seront utiles par la suite.
Ensuite allez dans les reglages de votre app, et ajoutez une url de redirection : http://localhost:8080/

ensuite ouvrez un terminal et entrez les commandes suivantes :
```export SPOTIPY_CLIENT_ID=entrez votre id client ici
export SPOTIPY_CLIENT_SECRET=entrez votre id client secret ici
export SPOTIPY_REDIRECT_URI=http://localhost:8080```

Ensuite vous pouvez lancer le script pour tester les fonctions implémentées.
N'oubliez pas de lancer un son sur spotify, dans le cas contraire les fonctions risqueraient de retourner une erreur.