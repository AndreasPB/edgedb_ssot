CREATE MIGRATION m1faattezah627k544elwato3m4dgjbyyz3nqn2huxeovh2luv4eua
    ONTO m1ccbjebnaeoq2hki3ma35lw5pkf6sadomsjyuehxzgecxq2h4uwgq
{
  ALTER TYPE default::Movie {
      ALTER PROPERTY title {
          SET REQUIRED USING ('Untitled');
      };
  };
};
