/*
 *  Created by Martin on 17/02/2017.
 *
 *  Distributed under the Boost Software License, Version 1.0. (See accompanying
 *  file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
 */

#include "catch.hpp"


// This is a minimal example for an issue we have found in 1.7.0
struct foo {
    int i;
};

template <typename T>
bool operator==(const T& val, foo f){
    return val == f.i;
}

TEST_CASE("#809") {
    foo f; f.i = 42;
    REQUIRE(42 == f);
}
