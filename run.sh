# poetry env activate
sudo docker compose up --build --force-recreate --renew-anon-volumes postgres -d
sleep 5 # wiating for db to start up
if [ -z "$(sudo docker ps -a | grep pgadmin)" ]; then
    sudo docker compose up pgadmin -d
fi
poetry run alembic upgrade head
