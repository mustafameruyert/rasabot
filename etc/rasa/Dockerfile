# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:1.10.0

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements, if necessary (uncomment next line)
# COPY actions/requirements-actions.txt ./

# Change back to root user to install dependencies
USER root

# Install extra requirements for actions code, if necessary (uncomment next line)
RUN pip install --no-cache-dir google
RUN pip install --no-cache-dir newspaper3k
#RUN pip install --no-cache-dir appdirs
#RUN pip install --no-cache-dir tensorflow-gpu==2.1.0
#RUN pip install --no-cache-dir tensorflow==2.1.0
#RUN pip install --no-cache-dir torch torchvision
#RUN pip install --no-cache-dir ipywidgets
#RUN pip install --no-cache-dir transformers
#RUN pip install --no-cache-dir -r /app/actions/requirements-actions.txt
#RUN apt-get update && apt-get install -y git
#RUN git clone https://git.dar.kz/DRysbek/qa.git
#CMD [ "python3", "qa/setup_qa.py" ]

# Copy actions folder to working directory
COPY ./actions /app/actions

# By best practices, don't run the code with root user
USER 1001

CMD ["start", "--actions", "actions"]
