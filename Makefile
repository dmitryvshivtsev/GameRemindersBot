.PHONY: docker

docker:
	docker stop sport_bot
	docker rm sport_bot
	docker rmi sport:bot
	docker build -t sport_bot:last .
	docker run --name sport_bot -d sport_bot:last
