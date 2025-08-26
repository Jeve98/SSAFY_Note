import React, { useState, useEffect, useRef } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { RootState, AppDispatch } from '../store/store';
import { addMessage, postMessage } from '../store/chatSlice';
import Message from '../components/Message';
import './ChatPage.css';

const ChatPage = () => {
  const [input, setInput] = useState('');
  const [imagePreview, setImagePreview] = useState<string | null>(null);
  const dispatch = useDispatch<AppDispatch>();
  const { messages, status } = useSelector((state: RootState) => state.chat);
  const chatHistoryRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Scroll to the bottom of the chat history when messages change
    if (chatHistoryRef.current) {
      chatHistoryRef.current.scrollTop = chatHistoryRef.current.scrollHeight;
    }
  }, [messages]);

  const handleSendMessage = () => {
    if (input.trim() === '' && !imagePreview) return;

    const userMessage = {
      id: Date.now().toString(),
      text: input,
      sender: 'user' as 'user',
      image: imagePreview || undefined,
    };

    dispatch(addMessage(userMessage));
    dispatch(postMessage({ text: input, image: imagePreview || undefined }));

    setInput('');
    setImagePreview(null);
  };

  const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      const reader = new FileReader();
      reader.onload = (event) => {
        setImagePreview(event.target?.result as string);
      };
      reader.readAsDataURL(e.target.files[0]);
    }
  };

  const handleCancelImage = () => {
    setImagePreview(null);
  };

  return (
    <div className="chat-container">
      <div className="chat-history" ref={chatHistoryRef}>
        {messages.map((msg) => (
          <Message key={msg.id} text={msg.text} sender={msg.sender} image={msg.image} />
        ))}
        {status === 'loading' && <Message sender="ai" text="..." />}
      </div>
      <div className="chat-input-area">
        {imagePreview && (
          <div className="image-preview-container">
            <img src={imagePreview} alt="Preview" className="image-preview" />
            <button onClick={handleCancelImage} className="btn btn-danger btn-sm cancel-btn">X</button>
          </div>
        )}
        <input type="file" id="image-upload" accept="image/*" onChange={handleImageChange} style={{ display: 'none' }} />
        <label htmlFor="image-upload" className="btn btn-secondary">🖼️</label>
        <input 
          type="text" 
          className="form-control" 
          placeholder="메시지를 입력하세요..." 
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
          disabled={status === 'loading'}
        />
        <button className="btn btn-primary" onClick={handleSendMessage} disabled={status === 'loading'}>
          {status === 'loading' ? '전송중...' : '전송'}
        </button>
      </div>
    </div>
  );
};

export default ChatPage;
