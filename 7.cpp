#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

class FlightGraph {
private:
    vector<vector<int>> adjMatrix;
    vector<string> cities;
    int numCities;
public:
    FlightGraph(int n) {
        numCities = n;
        adjMatrix.resize(n, vector<int>(n, 0));
        cities.resize(n);
    }

    void inputCities() {
        cout << "Enter names of " << numCities << " cities:\n";
        for (int i = 0; i < numCities; i++) {
            cout << "City " << i + 1 << ": ";
            cin >> cities[i];
        }
    }

    void addFlightPaths() {
        int time;
        cout << "Enter travel time in hours between cities (enter 0 if no direct flight):\n";
        for (int i = 0; i < numCities; i++) {
            for (int j = 0; j < numCities; j++) {
                if (i != j) {
                    cout << "Time from " << cities[i] << " to " << cities[j] << ": ";
                    cin >> time;
                    while (time < 0) {
                        cout << "Invalid time. Please enter a non-negative value: ";
                        cin >> time;
                    }
                    adjMatrix[i][j] = time;
                }
            }
        }
    }

    void displayAdjMatrix() {
        cout << "\nAdjacency Matrix Representation (Travel time in hours):\n";
        cout << setw(10) << "";
        for (const auto& city : cities) {
            cout << setw(10) << city;
        }
        cout << "\n";
        for (int i = 0; i < numCities; i++) {
            cout << setw(10) << cities[i];
            for (int j = 0; j < numCities; j++) {
                cout << setw(10) << adjMatrix[i][j];
            }
            cout << endl;
        }
    }
};

int main() {
    int n;
    cout << "Enter number of cities: ";
    cin >> n;
    FlightGraph graph(n);
    graph.inputCities();
    graph.addFlightPaths();
    graph.displayAdjMatrix();
    return 0;
}
