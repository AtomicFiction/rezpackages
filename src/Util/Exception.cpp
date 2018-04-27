//-*****************************************************************************
// Copyright 2015 Christopher Jon Horvath
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//-*****************************************************************************

#include "Exception.h"

namespace EncinoWaves {
namespace Util {

//-*****************************************************************************
void __EWAV_DEBUG_ASSERT_FAIL(const char* msg) throw() {
  std::cerr << msg << std::endl;
  abort();
}

}  // namespace Util
}  // namespace EncinoWaves
