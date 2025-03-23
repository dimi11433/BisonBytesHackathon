'use client';
const ButtonSeq = ({updateSeq}: {updateSeq: Function}) => {
  return (
    <button
      className="bttn"
      onClick={() => {
        updateSeq(prompt("Enter your sequence"));
      }}
    >
      Submit sequence
    </button>
  );
};

export default ButtonSeq;
