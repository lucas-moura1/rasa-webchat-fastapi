
FROM frostming/pdm

WORKDIR /app

COPY . .

USER root

RUN rm -rf __pypackages__

RUN pdm install

EXPOSE 8000

# CMD [ "pdm", "run", "dev" ]
