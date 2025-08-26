import React from 'react';

const SignupPage = () => {
  return (
    <div className="container mt-5" style={{ maxWidth: '500px' }}>
      <h2 className="text-center mb-4">회원가입</h2>
      <form>
        <div className="mb-3">
          <label htmlFor="emailInput" className="form-label">이메일 주소</label>
          <input type="email" className="form-control" id="emailInput" />
        </div>
        <div className="mb-3">
          <label htmlFor="passwordInput" className="form-label">비밀번호</label>
          <input type="password" className="form-control" id="passwordInput" />
        </div>
        <div className="mb-3">
          <label htmlFor="confirmPasswordInput" className="form-label">비밀번호 확인</label>
          <input type="password" className="form-control" id="confirmPasswordInput" />
        </div>
        <button type="submit" className="btn btn-primary w-100">회원가입</button>
      </form>
    </div>
  );
};

export default SignupPage;
