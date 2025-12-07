import Message from "./Message";
import Alert from "./components/Alert";
import ListGroup from "./components/ListGroup";
import Button from "./components/Button";
import { useState } from "react";

// let items = ["New York", "San Fransico", "Tokyo", "London", "Paris"];

// function App() {
//   const handleSelectItem = (item: string) => {
//     console.log(item);
//   };

//   return (
//     <div>
//       <ListGroup
//         items={items}
//         heading="Cities"
//         onSelectItem={handleSelectItem}
//       />
//     </div>
//   );
// }

function App() {
  const [alertVisible, setAlertVisibility] = useState(false);
  return (
    <div>
      {alertVisible && (
        <Alert onClose={() => setAlertVisibility(false)}>Hello World</Alert>
      )}
      <Button onClick={() => setAlertVisibility(true)}>My Button</Button>
    </div>
  );
}

export default App;
