import React from 'react';

const LoginPage = () => {
  return (
    <div className="container mt-5" style={{ maxWidth: '500px' }}>
      <h2 className="text-center mb-4">로그인</h2>
      <form>
        <div className="mb-3">
          <label htmlFor="emailInput" className="form-label">이메일 주소</label>
          <input type="email" className="form-control" id="emailInput" />
        </div>
        <div className="mb-3">
          <label htmlFor="passwordInput" className="form-label">비밀번호</label>
          <input type="password" className="form-control" id="passwordInput" />
        </div>
        <button type="submit" className="btn btn-primary w-100">로그인</button>
      </form>
    </div>
  );
};

export default LoginPage;
