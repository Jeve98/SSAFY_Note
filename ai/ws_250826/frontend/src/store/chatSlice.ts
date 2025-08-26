import { createSlice, createAsyncThunk, PayloadAction } from '@reduxjs/toolkit';
import apiClient from '../api/client';

interface Message {
  id: string;
  text: string;
  sender: 'user' | 'ai';
  image?: string;
}

interface ChatState {
  messages: Message[];
  status: 'idle' | 'loading' | 'succeeded' | 'failed';
}

const initialState: ChatState = {
  messages: [
    {
      id: '1',
      text: '안녕하세요! SSAFY 챗봇입니다. 무엇을 도와드릴까요?',
      sender: 'ai',
    },
  ],
  status: 'idle',
};

export const postMessage = createAsyncThunk(
  'chat/postMessage',
  async (message: { text: string; image?: string }) => {
    const response = await apiClient.post('/api/chat', { message });
    return response.data;
  }
);

const chatSlice = createSlice({
  name: 'chat',
  initialState,
  reducers: {
    addMessage: (state, action: PayloadAction<Message>) => {
      state.messages.push(action.payload);
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(postMessage.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(postMessage.fulfilled, (state, action: PayloadAction<Message>) => {
        state.status = 'succeeded';
        state.messages.push(action.payload);
      })
      .addCase(postMessage.rejected, (state) => {
        state.status = 'failed';
        // Optionally, add a message to the chat indicating the error
        state.messages.push({
          id: Date.now().toString(),
          text: '죄송합니다, 메시지 전송에 실패했습니다.',
          sender: 'ai',
        });
      });
  },
});

export const { addMessage } = chatSlice.actions;
export default chatSlice.reducer;
