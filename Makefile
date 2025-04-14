
build: zip exe

release: build
	cp tmt.zip build/tmt

install: build
	cp tmt.zip ~/.local/bin/tmt

zip: clean
	cd tmt && zip -r ../tmt-temp.zip . -x "*/__pycache__/*"

exe:
	echo '#!/usr/bin/env python3' | cat - tmt-temp.zip > tmt.zip && chmod +x tmt.zip
	rm tmt-temp.zip

deploy: build
	cp tmt.zip ~/.local/bin/tmt

clean:
	rm -f tmt-temp.zip tmt.zip
	rm -rf tmt/**/*.pyc
	rm -rf tmt/**/__pycache__
