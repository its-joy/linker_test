build:
	docker build --force-rm $(options) -t linkers_website .
# build docker image
build-prod:
# build only the production image
	$(MAKE) build options="--target production"

# command to start up our docker image
# remove files that from previous run that we don't need 
compose-start:
	docker-compose up --remove-orphans $(options)

# remove any networks or containers that were running
compose-stop:
	docker-compose down --remove-orphans $(options)

# can use this command to make migrations
compose-manage-py:
	docker-compose run --rm $(options) website python manage.py $(cmd)