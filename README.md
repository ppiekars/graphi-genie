# GraphiGenie

Welcome to GraphiGenie!

GraphiGenie is a powerful web application that utilizes stable diffusion to generate high-quality, realistic images from text descriptions. With GraphiGenie, you can easily and quickly transform textual descriptions into beautiful, vivid images that bring your words to life. Our state-of-the-art algorithms use cutting-edge techniques to synthesize images that closely match the details and context of your textual input. Whether you are a writer, designer, or content creator, GraphiGenie provides you with an efficient and effective tool to enhance your projects with stunning visual imagery.

## Getting Started

To get started with GraphiGenie, follow these simple steps:

### 1. Clone the GitHub repo

Clone the GitHub repository to your local machine using the following command:

```bash
git clone https://github.com/ppiekars/graphi-genie.git
```

### 2. Navigate to the directory

Navigate to the root directory of the cloned repository:

```bash
cd graphi-genie
```

### 3. Install the requirements

Create a virtual environment (recommended) and install the required dependencies from `requirements.txt` using pip:

```bash
python3 -m venv env
source env/bin/activate
pip install -r be/requirements.txt
```

### 4. Run the server

Start the server using the following command:

```bash
uvicorn be.main:app --reload
```

The server will be running at http://localhost:8000.

### 5. Explore the API

To explore the API, navigate to the default FastAPI docs endpoint at http://localhost:8000/docs. You can use the interactive documentation to test the API endpoints and see how the app works. 

That's it! You're ready to start upscaling your videos with GraphiGenie.

## Using with Celery

### 1. Message broker

Celery requires a solution to send and receive messages; usually this comes in the form of a separate service called a message broker.

We will use RabbitMQ.

The easiest way to get RabbitMQ started is by running it with docker:

```bash
docker run -d -p 5672:5672 rabbitmq
```

Alternatively you can install RabbitMQ with brew:

```bash
brew install rabbitmq
```

### 2. Starting the worker and the dashboard

Then, start the worker and flower in separate terminals:

```bash
celery -A be.main.celery worker --loglevel=info --concurrency=2
```

Concurrency defines how many processes can be handled at the same time. Since we are running high intensity jobs, it is good to limit this number.

```bash
celery -A be.main.celery flower --port=5555 
```

You can now navigate to http://localhost:5555 to see the Flower dashboard.