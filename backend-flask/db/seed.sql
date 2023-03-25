-- this file was manually created
INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('Andrew Brown', 'sample@test.com', 'andrewbrown' ,'MOCK'),
  ('PRATIK SINHA', 'pratik.sinha08+zxc@gmail.com', 'pratiksinha' ,'MOCK'),
  ('Andrew Bayko', 'example@gmail.com', 'bayko' ,'MOCK');
  ('Londo Mollari','lmollari@centari.com' ,'londo' ,'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'andrewbrown' LIMIT 1),
    (SELECT uuid from public.users WHERE users.handle = 'pratiksinha' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )
