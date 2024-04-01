all: game/icon.ico game/icon.icns

game/icon.ico: game/gui/window_icon.webp
	convert $< -define icon:auto-resize=256,128,48,32,16 $@

game/icon.icns: game/gui/window_icon.webp
	mkdir -p game.iconset
	convert $< -resize 1024x1024 game.iconset/icon_512x512@2x.png
	convert $< -resize 512x512 game.iconset/icon_512x512.png
	convert $< -resize 512x512 game.iconset/icon_256x256@2x.png
	convert $< -resize 256x256 game.iconset/icon_256x256.png
	convert $< -resize 256x256 game.iconset/icon_128x128@2x.png
	convert $< -resize 128x128 game.iconset/icon_128x128.png
	convert $< -resize 64x64 game.iconset/icon_32x32@2x.png
	convert $< -resize 32x32 game.iconset/icon_32x32.png
	convert $< -resize 32x32 game.iconset/icon_16x16@2x.png
	convert $< -resize 16x16 game.iconset/icon_16x16.png
	icnsutil -c icns -o $@ game.iconset
	rm -rf game.iconset

clean:
	rm -f game/icon.ico game/icon.icns game.iconset

.PHONY: all clean
