import logo from "./logo.svg";
import MyHeader from "./MyHeader";
import Counter from "./Counter";
import Container from "./Container";

function App() {
  const countProps = {
    a: 1,
    b: 2,
    c: 3,
    d: 4,
    e: 5,
    num: 10,
  };

  return (
    <Container>
      <div className="App">
        <MyHeader />
        <Counter {...countProps} />
      </div>
    </Container>
  );
}

export default App;
