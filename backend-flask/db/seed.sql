-- this file was manually created
INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('PRATIK SINHA', 'pratik.sinha08+zxc@gmail.com', 'pratiksinha' ,'MOCK'),
  ('Pratik Sinha', 'pratiksinha@mailinator.com', 'pratiksinha' ,'MOCK'),
  ('Michael Corleone', 'michaelcorleone@mailinator.com', 'michaelcorleone' ,'MOCK'),
  ('Andrew Brown', 'sample@test.com', 'andrewbrown' ,'MOCK'),
  ('Londo Mollari','lmollari@centari.com' ,'londo' ,'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'pratiksinha' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  ),
  (
    (SELECT uuid from public.users WHERE users.handle = 'michaelcorleone' LIMIT 1),
    'Michael Corleone wrote this new data, CAPICHE!',
    current_timestamp + interval '10 day'
  ),
  (
    (SELECT uuid from public.users WHERE users.handle = 'pratiksinha' LIMIT 1),
    'Different Pratik added this CRUD',
    current_timestamp + interval '10 day'
  );