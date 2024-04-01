all: icon.ico icon.icns

game/icon.ico: game/gui/window_icon.webp
	convert $< -define icon:auto-resize=256,128,48,32,16 $@

game/icon.icns: game/gui/window_icon.webp
	mkdir -p icon.iconset
	convert $< -resize 1024x1024 icon.iconset/icon_512x512@2x.png
	convert $< -resize 512x512 icon.iconset/icon_512x512.png
	convert $< -resize 512x512 icon.iconset/icon_256x256@2x.png
	convert $< -resize 256x256 icon.iconset/icon_256x256.png
	convert $< -resize 256x256 icon.iconset/icon_128x128@2x.png
	convert $< -resize 128x128 icon.iconset/icon_128x128.png
	convert $< -resize 64x64 icon.iconset/icon_32x32@2x.png
	convert $< -resize 32x32 icon.iconset/icon_32x32.png
	convert $< -resize 32x32 icon.iconset/icon_16x16@2x.png
	convert $< -resize 16x16 icon.iconset/icon_16x16.png
	icnsutil -c icns -o $@ icon.iconset
	rm -rf icon.iconset

clean:
	rm -f icon.ico icon.icns icon.iconset

.PHONY: all clean
