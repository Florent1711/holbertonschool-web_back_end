export default function getNeighbourhoodsList() {
  this.sanFranciscoNeighbourhoods = ['SOMA', 'Union Square'];

  const self = this;
  this.addNeighborhood = (newNeighbourhood) => {
    self.sanFranciscoNeighbourhoods.push(newNeighbourhood);
    return self.sanFranciscoNeighbourhoods;
  };
}
