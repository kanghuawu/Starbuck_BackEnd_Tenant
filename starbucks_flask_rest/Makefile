clean:
	find . -name "*.pyc" -exec rm -rf {} \;

docker-build: 
	docker build -t mystarbucks .
	docker images

docker-clean:
	docker stop mystarbucks
	docker rm mystarbucks
	docker rmi mystarbucks

docker-run:
	docker run --name mystarbucks -td mystarbucks
	docker ps

docker-run-host:
	docker run --name mystarbucks -td --net=host mystarbucks
	docker ps

docker-run-bridge:
	docker run --name mystarbucks -td -p 90:9090 mystarbucks
	docker ps

docker-network:
	docker network inspect host
	docker network inspect bridge

docker-stop:
	docker stop mystarbucks
	docker rm mystarbucks

docker-shell:
	docker exec -it mystarbucks bash 