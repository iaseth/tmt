
build: zip exe

zip:
	cd tmt && zip -r ../tmt-temp.zip . -x "*/__pycache__/*"

exe:
	echo '#!/usr/bin/env python3' | cat - tmt-temp.zip > tmt.zip && chmod +x tmt.zip
	rm tmt-temp.zip

deploy: build
	cp tmt.zip ~/dev/bin/tmt

clean:
	rm -f tmt-temp.zip tmt.zip
	rm -rf **/__pycache__
