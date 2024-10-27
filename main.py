from flask import Flask, render_template
import random
import socket

app = Flask(__name__)

def generate_random_values():
    return {
        "temperature": round(random.uniform(15, 35), 1),
        "power_usage": round(random.uniform(100, 500), 2),
        "solar_generation": round(random.uniform(0, 100), 2),
        "water_usage": round(random.uniform(50, 200), 2),
        "air_quality": random.randint(0, 100),
        "vibe": random.choice(["Good", "Neutral", "Bad"]),
        "feng_shui": random.randint(1, 10),
        "hostname": socket.gethostname(),
        "cat_happiness": random.choice(["Purring", "Meowing", "Napping", "Plotting World Domination"]),
        "coffee_pot_fullness": f"{random.randint(0, 100)}%"
    }

def generate_graph_data():
    return {
        "line_data": [random.randint(0, 100) for _ in range(7)],
        "bar_data": [random.randint(0, 100) for _ in range(5)],
        "pie_data": [random.randint(1, 30) for _ in range(4)]
    }

@app.route('/')
def index():
    values = generate_random_values()
    graph_data = generate_graph_data()
    return render_template('index.html', values=values, graph_data=graph_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9100)
