import React from 'react';
import './Message.css';

interface MessageProps {
  text: string;
  sender: 'user' | 'ai';
  image?: string;
}

const Message: React.FC<MessageProps> = ({ text, sender, image }) => {
  const messageClass = sender === 'user' ? 'user-message' : 'ai-message';

  return (
    <div className={`message-container ${messageClass}`}>
      <div className="message-bubble">
        {text}
        {image && <img src={image} alt="chat content" className="message-image"/>}
      </div>
    </div>
  );
};

export default Message;