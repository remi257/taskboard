FROM python:3.12.4-bookworm

WORKDIR /workspace

ENV DISCORD_TOKEN=foo
ENV CONNECTION_STRING=foo

COPY . .
RUN pip install -r requirements.txt



CMD python ./bot.py
# CMD ["py" "./discord.py"]