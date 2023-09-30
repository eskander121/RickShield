#!/bin/bash

read -p "please if you have already installed howdy check the code of sleepinstaller.sh and remove the howdy config step
__________________________________________________________________________________________________________________________
"
cd files 
cp 'KGzngdVKbrk_Rick-Astley---Never-Gonna-Give-You-Up.wav'  '/home/'$USER'/'
cp lm.py '/home/'$USER'/'
cp si.sh '/home/'$USER'/'
cd si
cp pe.py '/home/'$USER'/'
cp ki.py '/home/'$USER'/'
cd ..
cd lm
cp sleep.py '/home/'$USER'/'
cp s.sh '/home/'$USER'/'
cp obs.py '/home/'$USER'/'
cd sleep 
cp b.py '/home/'$USER'/'
cp hj.py '/home/'$USER'/'
cp uy.py '/home/'$USER'/'
cp x.py '/home/'$USER'/'
cd ..
cd s
cp k.py '/home/'$USER'/'
cp pe.py '/home/'$USER'/'
pip install playsound
pulseaudio -k && sudo alsa force-reload
read -p "please before you click enter set a keyboard shortcut for lm.py choose a key combination that later will be used to suspend your laptop
_______________________________________________________________________________________________________________________________________________
"
read -p "and also set a keyboard shortcut to execute si.sh this shortcut will be used to stop the rickroll if you are authenticated press enter if your done
______________________________________________________________________________________________________________________________________________________
"
# howdy    config
read -p "press enter to install howdy howdy is a software for face authentication. read more at there github https://github.com/boltgolt/howdy
____________________________________________________________________________________________________________________________________________
"
sudo add-apt-repository ppa:boltgolt/howdy
sudo apt update
sudo apt install howdy
cd '/home/'$USER'/RickShield/myscript'
cd files

sudo chmod -R a+rwX /usr/lib/security/howdy/recorders
sudo cp cli.py /lib/security/howdy
sudo cp -r cli /lib/security/howdy
sudo cp snapshot.py /lib/security/howdy
read -p "_____________________________________________
next your face will be added but first fill in a name for your face and then click enter then look in the camera until done     press enter to continue 
_____________________________________________________________________________________________________________________________________________________________
"
sudo howdy add 
# howdy config end
cd '/home/'$USER'/RickShield/myscript'
cd files
cp k.desktop '/home/'$USER'/RickShield/Documents'
# obs part
sudo apt install obs-studio
# obs part end
#installing pm-utils
sudo apt install pm-utils
read -p 'to also capture video you need to launch obs and add source video then click ok and adjust the size of the webcam as large as posible    then click enter
_________________________________________________________________________________________________________________________________________________________________'
read -p 'read the ReadMe for info how the script works

and there is a good chanse you will need to change the howdy config file you can do this by running sudo howdy config  '

echo done ':)'



