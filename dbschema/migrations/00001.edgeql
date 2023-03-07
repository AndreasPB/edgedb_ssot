CREATE MIGRATION m1ccbjebnaeoq2hki3ma35lw5pkf6sadomsjyuehxzgecxq2h4uwgq
    ONTO initial
{
  CREATE TYPE default::Person {
      CREATE REQUIRED PROPERTY name -> std::str;
  };
  CREATE TYPE default::Movie {
      CREATE MULTI LINK actors -> default::Person;
      CREATE PROPERTY title -> std::str;
  };
};
