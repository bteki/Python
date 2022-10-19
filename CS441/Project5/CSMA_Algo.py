from random import randint

def main():

    prob = int(input("Select 25%, 50%, or 75% as your probality: "))
    # prob = 25
    host = 2
    packet = 500
    '''
    host == 3:
    packet = 333
    host == 4:
    packet = 250
    host == 5:
    packet = 200
    '''

    host_name = ['host1', 'host2', 'host3', 'host4', 'host5']

    table_host = []
    table_host_prob = []
    table_packets = []

    for i in range(host):
        table_host.append(host_name[i])
        table_host_prob.append(100)
        table_packets.append(packet)

        trans_time = 0
        collision = 0
        host_index = 0

        while True:
            host_trans = 0
            for i in range(len(table_host)):
                table_host_prob[i] = randint(1,100)

                if table_host_prob[i] <= prob:
                    host_trans += 1

            match host_trans:
                case 1:
                    host_index = table_host_prob.index(min(table_host_prob))
                    table_packets[host_index] -= 1
                    trans_time += 1

                    if table_packets[host_index] == 0:
                        table_host.pop(host_index)
                        table_host_prob.pop(host_index)
                        table_packets.pop(host_index)

                    if len(table_host) == 0:
                        print("Transmission time: {}, Collision: {}.".format(trans_time, collision))
                        return False

                # case 0:
                #    trans_time += 1

                case _:
                    trans_time += 1
                    collision += 1

main()



