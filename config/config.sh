function docs() {
	dialog --title "Documentation" --textbox KivyDexel/config/docs.txt 20 70
}


    HEIGHT=13
    WIDTH=45
    CHOICE_HEIGHT=10
    BACKTITLE=$(gecpc "By Lightning" "+")
    TITLE="Config-Menu"
    MENU="Available Options"

    OPTIONS=(1 "Install Dependencies"
             2 "Install Firefox"
             3 "Update Apt-Get"
             4 "Documentation-- README!!!"
             5 "Gimme Container Terminal!!")

    CHOICE=$(dialog --clear --cancel-label "Exit" \
                    --backtitle "$BACKTITLE" \
                    --title "$TITLE" \
                    --menu "$MENU" \
                    $HEIGHT $WIDTH $CHOICE_HEIGHT \
                    "${OPTIONS[@]}" \
                    2>&1 >/dev/tty)

    case $CHOICE in
        1)clear && apt-get install -y python3-pip && pip3 install wget pytube pillow kivy kivymd ffpyplayer && bash /KivyDexel/config/config.sh;;
        2)clear && apt-get install firefox && bash /KivyDexel/config/config.sh;;
        3)clear && apt-get update && bash /KivyDexel/config/config.sh;;
        4)clear && docs && bash /KivyDexel/config/config.sh;;
    	5)clear && bash;;
        *)bash /KivyDexel/config/config.sh;;
    esac