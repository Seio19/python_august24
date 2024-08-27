def load_balancing(requests):
    servers=[0] * len(requests)
    server_requests ={i : 0 for i in range(len(requests))}
    requests.sort(key=lambda x: x[0])

    for arrival_time, load in requests:
        while servers and servers[0]<= arrival_time:
            server_index=servers.pop(0)
            server_counts[server_index] += 1
            servers.append((arrival_time+load, len(servers)))
    return server_counts




