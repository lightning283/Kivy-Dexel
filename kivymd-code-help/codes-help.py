Image :
	source : "res/card_house.png"
	allow_stretch: True
	keep_ratio: True
	size_hint_y: None
	size_hint_x: None
	width: self.parent.width
	height: self.parent.width/self.image_ratio



MDFloatLayout:
    MDCard:
        orientation: "vertical" #give any (vertical or horizontal)
        size_hint: None, None
        size: "280dp", "535dp" # size of the card
        pos_hint: {"center_x": .5, "center_y": .5}
        Video:
            id : vid_anime_amv #give any name without ''
            source : ''
            allow_stretch :True
            options : {'eos': 'stop'}


on_press: #button to control the video playback
	setattr(vid_anime_amv, 'source', '##give source of the video here')
	setattr(vid_anime_amv, 'state', 'play')