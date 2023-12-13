import React, { useState } from "react";
import OddEvenResult from "./oddEvenResult";

const Counter = ({ num2 }) => {
  const [count, setCount] = useState(num2);

  const onIncrease = () => {
    setCount(count + 1);
  };

  const onDecrease = () => {
    setCount(count - 1);
  };
  return (
    <div>
      <h2>{count}</h2>
      <button onClick={onIncrease}>+</button>
      <button onClick={onDecrease}>-</button>
      <OddEvenResult count={count} />
    </div>
  );
};

Counter.defaultProps = {
  num2: 0,
};

export default Counter;
