
build: zip exe

release: build
	cp tmt build/tmt

install: build
	cp tmt ~/.local/bin/

zip: clean
	cd tmtpy && zip -r ../tmt.zip . -x "*/__pycache__/*"

exe:
	echo '#!/usr/bin/env python3' | cat - tmt.zip > tmt && chmod +x tmt
	rm tmt.zip

deploy: build
	cp tmt ~/.local/bin/

clean:
	rm -f tmt.zip tmt
	rm -rf tmtpy/**/*.pyc
	rm -rf tmtpy/**/__pycache__
