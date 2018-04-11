/* globals gettext */
import React from 'react';
import { Button } from '@edx/paragon/static';
import StudentAccountDeletionModal from './StudentAccountDeletionModal';

export class StudentAccountDeletion extends React.Component {
  constructor(props) {
    super(props);
    this.closeDeletionModal = this.closeDeletionModal.bind(this);
    this.loadDeletionModal = this.loadDeletionModal.bind(this);
    this.state = {
      deletionModalOpen: false,
    };
  }

  closeDeletionModal() {
    console.log('Confirmation Modal Closed');
    document.getElementById('delete-account-btn').focus();
  }

  loadDeletionModal() {
    this.setState({ deletionModalOpen: true });
  }

  render() {
    const { deletionModalOpen } = this.state;

    return (
      <div>
        <h2>Delete My Account</h2>
        <span>We are sorry to see you go!</span>
        <span>Please note:</span>
        <span>If your account is deleted, ALL your data will be deleted. This includes:</span>
        <ul>
          <li>Credentials</li>
          <li>Certificates</li>
          <li>Program and Course data</li>
          <li>Profile data</li>
        </ul>
        <span>You will not be able to make a new account on edX with the same email address</span>
        <Button
          id="delete-account-btn"
          label={gettext('Delete My Account')}
          onClick={this.loadDeletionModal}
        />
        {deletionModalOpen && <StudentAccountDeletionModal onClose={this.closeDeletionModal} />}
      </div>
    );
  }
}
