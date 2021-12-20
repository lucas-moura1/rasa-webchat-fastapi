FROM rasa/rasa:2.8.16-full

WORKDIR /rasa-webchat

COPY . .

USER root

RUN pip install spacy && \
    pip install requests && \
    python -m spacy download pt_core_news_sm && \
    rasa telemetry disable

RUN rasa train

# EXPOSE 5050
