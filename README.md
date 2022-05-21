TODO:
  - Implement solar energy
  - Charging time vs connection time: wat als charging time > connection time?
  - Implement different charging strategies
    - Price driven
    - First come first serve
      - queue
    - Earliest latest feasible start time
      - max_num_charging kan beter, is nu niet afhankelijk van wat er nog meer staat op te laden
      - priority queue
  - Input analysis
  - Implement more statistics
    - Departure delays

Questions:
  - Price changes as events?
  - Does ELFS also try to actively minimize overloads
  - Expected departure time vs. real departure time

Assumptions:
  - Cars have no travel time between parking spaces
  - Charging capacity is never limited
  - Parking choices are random (not influenced by relative distance)
  - Cars only leave when they are fully charged
  - If connection time is shorter than charging time, it is extended as much as necessary
  - Cars do not care about the queue when picking a parking space for the FCFS strategy
  - Cars know the times of energy price changes
  - Cars do not queue for an empty parking spot
  - Rate change is applied instantly and starts a new proces

Model:
  - State: Parking lots, charging network, cars
  - Events:
    - Arrival
    - Parking
    - Start charging
    - Stop charging
    - (Expected finish)
    - Finished charging
    - Departure
    - Solar change
    - Price change
  - Event diagram:         arrival
                          /       \
                         V         V
          finished charging       departure
