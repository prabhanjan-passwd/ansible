---
- hosts: all
  tasks:
    -  command: awk -F: '/^awx/{print $2}' /etc/subuid
       register: awx_uid
    -  command: awk -F: '/^awx/{print $2}' /etc/subgid
       register: awx_gid
    -  ansible.builtin.user:
         name: awx
         uid: "{{ awx_uid.stdout }}"
         gid: "{{ awx_gid.stdout }}"
         state: present
