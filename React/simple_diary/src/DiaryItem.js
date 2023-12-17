import { useState, useRef } from "react";
const DiaryItem = ({
  onEdit,
  onDelete,
  id,
  author,
  content,
  emotion,
  created_date,
}) => {
  const handleDelete = () => {
    if (window.confirm(`${id}번째 일기를 정말 삭제하시겠습니까?`)) onDelete(id);
  };

  // 수정하기
  const [localContent, setLocalContent] = useState("");

  const [isEdit, setIsEdit] = useState(false);
  const localContentInput = useRef();

  const handleQuitEdit = () => {
    setIsEdit(false);
    setLocalContent(content);
  };

  const handleEdit = () => {
    if (localContent.length < 5) {
      localContentInput.current.focus();
      return;
    }
    window.confirm(`${id}번 째 일기를 수정하시겠습니까?`);
    onEdit(id, localContent);
    toggleIsEdit();
  };
  const toggleIsEdit = () => setIsEdit(!isEdit);
  return (
    <div className="DiaryItem">
      <div className="info">
        <span className="author_info">
          | 작성자 : {author} | 감정점수는 : {emotion} |
        </span>
        <br />
        <span className="date">{new Date(created_date).toLocaleString()}</span>
      </div>
      <div className="content">
        {isEdit ? (
          <>
            <textarea
              ref={localContentInput}
              value={localContent}
              onChange={(event) => setLocalContent(event.target.value)}
            />
          </>
        ) : (
          <>{content}</>
        )}
      </div>

      {isEdit ? (
        <>
          <button onClick={handleQuitEdit}>수정 취소</button>
          <button onClick={handleEdit}>수정완료</button>
        </>
      ) : (
        <>
          <button onClick={handleDelete}>삭제하기</button>

          <button onClick={toggleIsEdit}>수정하기</button>
        </>
      )}
    </div>
  );
};

export default DiaryItem;
